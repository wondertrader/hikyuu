/*
 *  Copyright(C) 2021 hikyuu.org
 *
 *  Create on: 2021-04-28
 *     Author: fasiondog
 */

#include "common/base64.h"
#include "user/model/TokenModel.h"
#include "TokenCache.h"
#include "RestErrorCode.h"
#include "RestHandle.h"
#include "filter.h"

namespace hku {

std::string createToken(uint64_t user_id) {
    Datetime now = Datetime::now();
    srand((unsigned)now.minute());
    int k = rand() % 1000;
    return base64_encode(fmt::format("{} {} {}", user_id, now, k), false);
}

struct TokenExpiredException : public hku::exception {
    TokenExpiredException(const std::string &msg) : hku::exception(msg) {}
};

void AuthorizeFilter(HttpHandle *handle) {
    std::string token = handle->getReqHeader("hku_token");
    HTTP_CHECK(!token.empty(), RestErrorCode::MISS_TOKEN, handle->_ctr("authorize", "Miss token"));

    std::string errmsg = handle->_ctr("authorize", "Invalid token");
    if (!TokenCache::have(token)) {
        TokenModel token_record;
        DB::getConnect()->load(token_record, fmt::format(R"(token="{}")", token));
        HTTP_CHECK(token_record.id() != 0, RestErrorCode::UNAUTHORIZED, errmsg);
        TokenCache::put(token);
    }

    try {
        std::string decode_token = base64_decode(token);
        auto pos = decode_token.find_first_of(" ");
        HTTP_CHECK(pos != std::string::npos, RestErrorCode::UNAUTHORIZED, errmsg);

        auto userid_str = decode_token.substr(0, pos);
        uint64_t user_id = 0;
        Datetime create_time;

        user_id = std::stoull(userid_str);
        auto d_pos = decode_token.find_last_of(" ");
        HTTP_CHECK(d_pos != std::string::npos, RestErrorCode::UNAUTHORIZED, errmsg);
        create_time = Datetime(decode_token.substr(pos + 1, d_pos - pos));

        Datetime expired_time = create_time + TimeDelta(30);
        Datetime now = Datetime::now();
        if (now > expired_time) {
            TokenCache::remove(token);
            {
                TokenModel token_record;
                auto con = DB::getConnect();
                TransAction trans(con);
                con->load(token_record, fmt::format(R"(token="{}")", token));
                con->exec(fmt::format(R"(delete from {} where token="{}")",
                                      TokenModel::getTableName(), token));
            }
            throw TokenExpiredException(handle->_ctr("authorize", "token is expired"));
        }

        RestHandle *rest_handle = dynamic_cast<RestHandle *>(handle);
        rest_handle->setCurrentUserId(user_id);

        if (expired_time - now <= TimeDelta(3)) {
            std::string new_token = createToken(user_id);
            TokenModel token_record;
            token_record.setToken(new_token);
            DB::getConnect()->save(token_record);
            TokenCache::put(new_token);
            rest_handle->setUpdateToken(new_token);
        }

    } catch (TokenExpiredException &e) {
        throw e;

    } catch (std::exception) {
        throw HttpError(RestErrorCode::UNAUTHORIZED, errmsg);
    }
}

}  // namespace hku
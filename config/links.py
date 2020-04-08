class Config:
    BASE_URL = "https://httpbin.org"

    # HEADERS = BASE_URL + "/headers"


class HttpMethods:
    DELETE = Config.BASE_URL + "/delete"
    GET = Config.BASE_URL + "/get"
    PATCH = Config.BASE_URL + "/patch"
    POST = Config.BASE_URL + "/post"
    PUT = Config.BASE_URL + "/put"


class StatusCodes:
    STATUS = Config.BASE_URL + "/status"  # /{codes} 100 200 300 400 500


class Request:
    HEADERS = Config.BASE_URL + "/put"
    IP = Config.BASE_URL + "/ip"
    USER_AGENT = Config.BASE_URL + "/user-agent"


class ResponseInspection:
    CACHE = Config.BASE_URL + "/cache"  # /{value}
    ETAG = Config.BASE_URL + "/etag"  # / {etag}
    RESPONSE_HEADERS = Config.BASE_URL + "/response-headers"


class Redirects:
    ABSOLUTE_REDIRECT = Config.BASE_URL + "/absolute-redirect"  # /{n}
    REDIRECT_TO = Config.BASE_URL + "/redirect-to"
    REDIRECT = Config.BASE_URL + "/redirect"  # /{n}
    RELATIVE_REDIRECT = Config.BASE_URL + "/relative-redirect"  # /{n}



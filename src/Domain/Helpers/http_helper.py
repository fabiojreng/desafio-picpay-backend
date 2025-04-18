from typing import Any


class HttpResponse:
    def __init__(self, status_code: int, body: dict[str, Any] = None):
        self.status_code = status_code
        self.body = body

    def to_dict(self) -> dict:
        return {"status_code": self.status_code, "body": self.body}


def server_error(error: Exception) -> HttpResponse:
    return HttpResponse(
        status_code=500,
        body={
            "type": "ServerError",
            "error": {"message": error},
        },
    ).to_dict()


def success(data: dict[str, Any]) -> HttpResponse:
    return HttpResponse(
        status_code=200,
        body={
            "type": "Success",
            "message": data.get("message"),
            "data": data.get("data"),
        },
    ).to_dict()


def created(data: dict[str, Any]) -> HttpResponse:
    return HttpResponse(
        status_code=201,
        body={
            "type": "Created",
            "message": data.get("message"),
            "data": data.get("data"),
        },
    ).to_dict()


def unprocessable_entity(error: Exception) -> HttpResponse:
    return HttpResponse(
        status_code=422,
        body={
            "type": "UnprocessableEntity",
            "error": {"message": error},
        },
    ).to_dict()


def not_found(error: Exception) -> HttpResponse:
    return HttpResponse(
        status_code=404,
        body={
            "type": "NotFound",
            "error": {"message": error},
        },
    ).to_dict()


def forbidden(error: Exception) -> HttpResponse:
    return HttpResponse(
        status_code=403,
        body={
            "type": "Forbidden",
            "error": {"message": error},
        },
    ).to_dict()


def no_content() -> HttpResponse:
    return HttpResponse(status_code=202, body=None).to_dict()


def unauthorized(error: Exception):
    return HttpResponse(
        status_code=401,
        body={"type": "Unauthorized", "error": {"message": error}},
    ).to_dict()

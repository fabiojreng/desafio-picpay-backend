from flask import Flask, request, json, Response
from flask_cors import CORS
from src.Infra.Http.interface_server_http import HttpServer


class FlaskAdapter(HttpServer):
    def __init__(self) -> None:
        self.__app = Flask(__name__)
        CORS(self.__app)

    def register(self, method, url, callback):
        view_name = f"{method.lower()}_{url.replace('/', '_')}_callback"

        def flask_callback(*args, **kwargs):
            try:
                if request.method == "GET":
                    if request.view_args:
                        output = callback(request.view_args)
                    else:
                        output = callback()

                else:
                    output = callback(request.json)
                return (
                    Response(
                        json.dumps(output, sort_keys=False),
                        mimetype="application/json",
                    ),
                    output["status_code"],
                )
            except Exception as e:
                return (
                    Response(
                        json.dumps(
                            {"status_code": 400, "body": str(e)}, sort_keys=False
                        ),
                        mimetype="application/json",
                    ),
                    400,
                )

        flask_callback.__name__ = view_name

        return self.__app.add_url_rule(
            rule=url, view_func=flask_callback, methods=[method.upper()]
        )

    def listen(self, port):
        print(f"SERVER RUNNING IN PORT {port}")
        return self.__app.run(port=port, debug=True)

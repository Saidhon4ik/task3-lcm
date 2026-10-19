import os
from math import gcd
from flask import Flask, request, Response

app = Flask(__name__)


@app.route("/" + os.environ["ROUTE"], methods=["GET"])
def lcm():
    x = request.args.get("x")
    y = request.args.get("y")

    if x is None or y is None:
        return Response("NaN", status=200, content_type="text/plain")

    if not x.isascii() or not y.isascii():
        return Response("NaN", status=200, content_type="text/plain")

    if not x.isdigit() or not y.isdigit():
        return Response("NaN", status=200, content_type="text/plain")

    x = int(x)
    y = int(y)

    if x == 0 or y == 0:
        return Response("0", status=200, content_type="text/plain")

    result = x * y // gcd(x, y)
    return Response(str(result), status=200, content_type="text/plain")


if __name__ == "__main__":
    app.run()

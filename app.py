import os
from flask import Flask

app = Flask(__name__)


@app.route("/" + os.environ["ROUTE"])
def lcm():
    return "hello"


if __name__ == "__main__":
    app.run()
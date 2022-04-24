from flask import Flask, render_template
from flask_socketio import SocketIO
import requests as req

app = Flask(__name__)
app.config["SECRET_KEY"] = "de16b73459bbfeceb67a01773f6684e7909e14d1ff61e5789a4c40067cb1a33c"
socketio = SocketIO(app)


@app.route("/")
def index():
    return render_template("index.html")


# @app.route("/led")
# def get():
#     return render_template("get.html")

# @app.route("/temp")
# def temp():
#     request

@socketio.on("led")
def handle_led(data):
    led_number = data["led"]
    led_status = data["status"]
    params = dict(led_status=led_status)
    r = req.get("http://192.168.1." + str(led_number) + "/led", params=params)


if __name__ == '__main__':
    socketio.run(app, port=8080, debug=True)

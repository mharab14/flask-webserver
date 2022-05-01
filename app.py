from flask import Flask, render_template, request
from flask_socketio import SocketIO
import requests as req

leds = {}
temp_hum = {}

app = Flask(__name__)
app.config["SECRET_KEY"] = "de16b73459bbfeceb67a01773f6684e7909e14d1ff61e5789a4c40067cb1a33c"
soio = SocketIO(app)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/temp", methods=["GET", "POST"])
def temp():
    data = request.get_json()
    soio.emit("temp", data)


@socketio.on("led")
def handle_led(data):
    led_number = data["led"]
    led_status = data["status"]
    params = dict(led_status=led_status)
    req_led = req.get("http://192.168.1" + "." + str(led_number) + "/led", params=params)
    print("code status :", req_led)

if __name__ == '__main__':
    socketio.run(app, port=8080, debug=True)


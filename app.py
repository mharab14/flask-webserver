import socketio
from flask import Flask, render_template, request
from flask_socketio import SocketIO
import requests as req

leds = {
    "102": [0, 0, 0],
    "103": [0, 0],
    "104": [0],
    "105": [0, 0],
    "106": [0],
    "107": [0, 0, 0]
}
temp_hum = {}
travel = False

app = Flask(__name__)
app.config["SECRET_KEY"] = "de16b73459bbfeceb67a01773f6684e7909e14d1ff61e5789a4c40067cb1a33c"
soio = SocketIO(app)


# ---------------------------------------------------------------------------

@app.route("/")
def index():
    return render_template("index.html", leds=leds)


# ---------------------------------------------------------------------------

@app.route("/temp", methods=["GET", "POST"])
def temp():
    data = request.get_json()
    soio.emit("temp", data)
    return "Ok"


# ---------------------------------------------------------------------------

@app.route("/security", methods=["GET", "POST"])
def security():
    data = request.get_json()
    if data["mode"] == "alarm":
        if data["thief"] == "1":
            soio.emit("thief", {"thief" : "1"})
    elif data["mode"] == "enter":
        soio.emit("enter", {"name" : data["name"]})
        travel = False
        # {"mode" : "alarm", "thief" : "1"|"0"}
        # {"mode" : "enter","door-status" : True|false, "name" : "amini"|"arab"}
# ---------------------------------------------------------------------------

@soio.on("led")
def handle_led(data):
    esp_number = str(data["esp"])
    led_number = int(data["led"])
    led_status = int(data["status"])
    leds[esp_number][led_number] = led_status
    params = dict(led_status=led_status)
    req_led = req.get("http://192.168.1" + "." + str(esp_number) + "/led" + str(led_number), params=params)
    print("code status :", req_led)


# ---------------------------------------------------------------------------
@soio.on("travel")
def travel_d(data):
    status = int(data["status"])
    travel = bool(status)
    req.get("http://192.168.1.101/travel", params={"status": status})

if __name__ == '__main__':
    socketio.run(app, port=8080, debug=True)

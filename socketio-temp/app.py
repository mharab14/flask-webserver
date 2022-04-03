from flask import Flask, render_template, request
from flask_socketio import SocketIO

app = Flask(__name__)
app.config["SECRET_KEY"] = "de16b73459bbfeceb67a01773f6684e7909e14d1ff61e5789a4c40067cb1a33c"
socketio = SocketIO(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/temp", methods=["GET", "POST"])
def temp():
	sensor = request.args.get("sensor")
	temp = request.args.get("temp")
	
	socketio.emit("temp", {"sensor" : sensor, "temp" : temp})
	return "ok"

@socketio.on('message')
def handleMessage(msg):
	print('Message: ' + msg["data"])
	socketio.emit("response", {"data" : "ok"})

if __name__ == '__main__':
	socketio.run(app, debug=True)
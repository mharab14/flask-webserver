from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
socketio = SocketIO(app, cors_allowed_origins='*')

@app.route("/")
def index():
    return render_template("index.html")

@socketio.on('message')
def handleMessage(msg):
	print('Message: ' + msg["data"])
	socketio.emit("response", {"data" : "ok"})

if __name__ == '__main__':
	socketio.run(app)
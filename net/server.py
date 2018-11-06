import time

from flask import Flask, render_template
from flask_socketio import SocketIO, emit

from model.gestureModel import GestureModel

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

gestureModel: GestureModel


@app.route('/')
def hello_world():
    return 'Hello World!'


@socketio.on('i')
def client_msg(value_i):
    print(value_i)

    emit("i_callback", "success get I")
    gestureModel.updateI(value_i)


def runServer(model):
    global gestureModel
    gestureModel = model
    socketio.run(app=app, port=5000)

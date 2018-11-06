import socket
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
def client_msgI(value_i):
    print(value_i)

    emit("i_callback", "success get I")
    gestureModel.updateI(value_i)


@socketio.on('q')
def client_msgQ(value_i):
    print(value_i)

    gestureModel.updateQ(value_i)


@socketio.on('bsRecord')
def client_msgBs(value_i):
    print(value_i)

    gestureModel.updateBsRecord(value_i)


def runServer(model):
    global gestureModel
    gestureModel = model
    socketio.run(app=app,host='0.0.0.0', port=5000)

def get_host_ip():

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()

    return ip

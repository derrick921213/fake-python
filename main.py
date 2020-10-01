from flask import Flask,request,abort,render_template,jsonify
from flask_socketio import SocketIO,send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


if __name__ == '__main__':
    socketio.run(app,debug=True)
    
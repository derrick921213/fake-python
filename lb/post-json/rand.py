from flask import Flask, render_template
from flask_socketio import SocketIO
import random

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)
 
@app.route('/')
def index():
    return render_template('index.html',async_mode=socketio.async_mode)
 
@socketio.on('connect', namespace='/test_conn')
def test_connect():
    print("Connected")
    #socketio.sleep(5)
    for i in range(1,10):
        t = random_int_list(1, 100, 10)
        socketio.emit('status_response',{'data1': t},namespace='/test_conn')
 
def random_int_list(start, stop, length):
    start, stop = (int(start), int(stop)) if start <= stop else (int(stop), int(start))
    length = int(abs(length)) if length else 0
    random_list = []
    for i in range(length):
        random_list.append(random.randint(start, stop))
    return random_list
 
if __name__ == '__main__':
    socketio.run(app, debug=True)
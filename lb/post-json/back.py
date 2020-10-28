from flask import Flask, request, abort, render_template, jsonify
from flask_socketio import SocketIO, emit
import subprocess

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


@app.route("/status", methods=['GET'])
def upload():
    if not request.json:
        abort(400)

    d = request.json.get("data")
    print("receive data:{}".format(d))
    # do something
    #p = subprocess.Popen(d,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT) 
    #for line in p.stdout.readlines(): 
    #    print (line.decode('utf-8')) 
    #    socketio.emit('status_response',{'data1': str(line.decode('utf-8'))},namespace='/test_conn')
    # 回傳給前端
    socketio.emit('status_response',{'data1': d},namespace='/test_conn')
    
    return jsonify({"response": "ok"})
    


@app.route("/")
def home():    
    return render_template('index.html', async_mode=socketio.async_mode)


if __name__ == "__main__":
    socketio.run(app, debug=False)
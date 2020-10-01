from flask import Flask, request, abort, render_template, jsonify
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)



@app.route("/",methods=['GET','POST'])
def home():
    if request.method == 'POST':
        data = request.form.get('test')
        socketio.emit('test',{'data1': data})
        print('\n'+data+'\n')
    return render_template('send.html', async_mode=socketio.async_mode)


if __name__ == "__main__":
    socketio.run(app, debug=False)
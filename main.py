'''from flask import Flask,request,abort,render_template,jsonify

from flask_socketio import SocketIO,send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


if __name__ == '__main__':
    socketio.run(app,debug=True)
'''
'''from lib.test.pr import pre
s = input('test:')
pre(s)
'''
import sys
from command import install,uninstall
cmd = ['--install','--uninstall','--help']
out=" "
try:
    one = sys.argv[1]
    if one in cmd:
        if one == '--install':
            install()
        elif one == '--uninstall':
            uninstall()
        else:
            out = out.join(cmd)
            print("Argvs: " + out)
    else:
        out = out.join(cmd)
        print("Argvs: " + out)
except IndexError:
    out = out.join(cmd)
    print("Argvs: " + out)




from flask_login import LoginManager,UserMixin,login_required,login_user,logout_user,current_user
from flask import Flask, request, abort, render_template, jsonify,url_for, redirect, flash
from flask.helpers import get_flashed_messages
from time import sleep
app = Flask(__name__)
app.config['SECRET_KEY'] = '4888b08b80cf4d2069ce4cd27f5d0ae6'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.session_protection = "strong"
login_manager.login_view = 'login'
login_manager.login_message = '請證明你並非來自黑暗草泥馬界'

class User(UserMixin):
    pass
@login_manager.user_loader
def user_loader(us):
    if us not in users:
        return
    user = User()
    user.id = us
    return user

@login_manager.request_loader
def request_loader(request):
    us = request.form.get('user_id')
    if us not in users:
        return
    user = User()
    user.id = us
    user.is_authenticated = request.form['password'] == users[us]['password']
    return user    
users ={'Me':{'password':'myself'},
        'derrick':{'password':'0170'}
}

@app.route('/login',methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    us = request.form['user_id']
    if (us in users) and (request.form['password'] == users[us]['password']):
        user = User()
        user.id = us
        login_user(user)
        return redirect(url_for('index'))
    else:
        flash('登入失敗了...')
        return render_template('login.html')+"<h3> %s </h3>" % get_flashed_messages()
@app.route('/logout')
def logout():
    us = current_user.get_id()
    logout_user()
    return render_template('login.html')

@app.route('/')
@login_required
def index():
    return render_template('test.html')

if __name__ == "__main__":
    app.run()
from flask import render_template, redirect, session, request
from flask_app import app           
# import the class from friend.py
from flask_app.models.user import User

@app.route('/')
def index():
    return redirect ('/users')
@app.route('/users')
def users():
    allusers=User.get_all()
    return render_template('users.html',users=allusers)

@app.route('/add/user')
def adduser():
    return render_template('form.html')

@app.route('/create/user', methods=['POST'])
def createuser():
    data={
        'firstname':request.form['firstname'],
        'lastname':request.form['lastname'],
        'email':request.form['email']

    }
    User.create_user(data)
    return redirect ('/')
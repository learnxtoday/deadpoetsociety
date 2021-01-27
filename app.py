from flask import Flask, flash, redirect, render_template, request, session, abort, url_for
import os

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return redirect(url_for('feed'))

@app.route('/feed')
def feed():
    if session.get('logged_in'):
        return "<h1>feed</h1>"
    else:
        return render_template('login.html')

@app.route("/profile")
def showProfile():
    uname = session.get('username')
    uname = uname.capitalize()
    return render_template('profile.html', uname=uname)                 #**locals()

@app.route('/login', methods=['POST'])
def do_admin_login():
    if request.form['password'] == 'password' and request.form['username'] == 'parth':
        session['logged_in'] = True
        session['username'] = request.form['username']
        return home()
    else:
        flash('wrong password!')
        return home()

@app.route('/logout')
def logout():
    session['logged_in'] = False
    return home()

if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True,host='0.0.0.0', port=4000)

from flask import Flask, flash, redirect, render_template, request, session, abort, url_for
from random import randint
import os

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return redirect(url_for('feed'))


#@app.route("/feed/<string:name>/")
@app.route("/feed/uname/")
@app.route('/feed')
def feed():
    if session.get('logged_in'):
        uname = session.get('username')
        uname = uname.capitalize()
        quotes = [ "'If people do not believe that mathematics is simple, it is only because they do not realize how complicated life is.' -- John Louis von Neumann ",
                "'Computer science is no more about computers than astronomy is about telescopes' --  Edsger Dtra ",
                "'To understand recursion you must first understand recursion..' -- Unknown",
                "'You look at things that are and ask, why? I dream of things that never were and ask, why not?' -- Unknown",
                "'Mathematics is the key and door to the sciences.' -- Galileo Galilei",
                "'Not everyone will understand your journey. Thats fine. Its not their journey to make sense of. Its yours.' -- Unknown"  ]
        randomNumber = randint(0,len(quotes)-1)
        quote = quotes[randomNumber]
        return render_template('members.html', **locals())
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

from flask import Flask, flash, redirect, render_template, request, session, abort, url_for
from random import randint


app = Flask(__name__)
app.config["DEBUG"] = True

'''
SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username="thenerdsuperuser",
    password="asdfghjkl;'",
    hostname="thenerdsuperuser.mysql.pythonanywhere-services.com",
    databasename="thenerdsuperuser$comments",
)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
'''
comments = []


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html", comments=comments)

    comments.append(request.form["contents"])
    return redirect(url_for('index'))


@app.route("/members/<string:name>/")
def getMember(name):
    quotes = [ "'If people do not believe that mathematics is simple, it is only because they do not realize how complicated life is.' -- John Louis von Neumann ",
            "'Computer science is no more about computers than astronomy is about telescopes' --  Edsger Dtra ",
            "'To understand recursion you must first understand recursion..' -- Unknown",
            "'You look at things that are and ask, why? I dream of things that never were and ask, why not?' -- Unknown",
            "'Mathematics is the key and door to the sciences.' -- Galileo Galilei",
            "'Not everyone will understand your journey. Thats fine. Its not their journey to make sense of. Its yours.' -- Unknown"  ]
    randomNumber = randint(0,len(quotes)-1)
    quote = quotes[randomNumber]
    name = name + " <= " + name[::-1]
    return render_template(
            'members.html',**locals()
        )

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=42069)

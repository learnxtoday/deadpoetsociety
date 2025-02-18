from flask import Flask, flash, redirect, render_template, request, session, abort, url_for


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


# SCRATCHBOARD
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("scratch_index.html", comments=comments)

    comments.append(request.form["contents"])
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)

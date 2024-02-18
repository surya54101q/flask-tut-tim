from flask import Blueprint , render_template , request , flash
from .models import User
auth = Blueprint("auth", __name__)


@auth.route("/login", methods = ["GET" , "POST"])
def login():
    data = request.form
    print(data)
    return render_template("login.html")


@auth.route("/logout", methods = ["GET" , "POST"])
def logout():
    return "logout"


@auth.route("/signup", methods = ["GET" , "POST"])
def sign_up():
    if request.method == "POST":
        email =request.form.get("email")
        firstname =request.form.get("firstname")
        password1 =request.form.get("password1")
        password2 =request.form.get("password2")

        if len(email)<4:
            flash("Email must be valid", category="error")
        elif len(firstname)<2:
            flash("First name is too short", category="error")

        elif password1 != password2:
            flash("Password is not matchin", category="error")
        elif len(password1)<7:
            flash("Password is too short", category="error")
        else:
            flash("Accoutn created", category="success")

    return render_template("signup.html")






    return render_template("signup.html")
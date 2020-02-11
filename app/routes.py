from app import app #import the Flask object app from the app package
from flask import render_template #import render_template function from flask
from app.forms import RegistrationForm

@app.route("/") #if you arent on a page complete the function below
@app.route("/index") # or if you are index page complete the function below
def index():
    return render_template("index.html", title="Home") # return the template base.html, where the variable title="Home"

@app.route("/register", methods=["GET", "POST"]) #if you are on register page
def register():
    form = RegistrationForm() #form is an instance of RegistrationForm class
    return render_template("register.html", title="Register", form=form)  # return the template register.html, where the variable title="Register"

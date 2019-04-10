from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too

@app.route("/", methods=["POST"])
def verify_data():
    username = request.form['username'].strip()
    password = request.form['password'].strip()
    verify = request.form['verify'].strip()
    email = request.form['email'].strip()

    user_name_error = ""
    password_error = ""
    verify_password_error = ""
    email_error = ""

    if username == "":
        user_name_error = "User Name cannot be blank."
    elif len(username) < 3:
        user_name_error = "User Name must be greater then 2 characters"
    elif len(username) > 20:
        user_name_error = "User Name must be less then 20 characters"
    elif username.find(" ") >= 0:
            user_name_error = "User Name cannot contain spaces"
    
    if password == "":
        password_error = "Password cannot be blank."
    elif len(password) < 3:
        password_error = "Password must be greater then 2 characters"
    elif len(password) > 20:
        password_error = "Password must be less then 20 characters"
    elif password.find(" ") >= 0:
        password_error = "Password cannot contain spaces"
    
    if verify == "":
        verify_password_error = "Verify password cannot be blank."
    elif password != verify:
        verify_password_error = "Password and verify password values dont match"

    if not(len(email) > 2 and len(email) < 20 and email.find("@") >= 0 and email.find(".") >=0 and email.find(" ") == -1):  
        email_error = "Invalid email address"

    if user_name_error == "" and password_error == "" and verify_password_error == "" and email_error == "":
        return render_template('welcome.html', username = username)
    else:
        return render_template('index.html', username = username, user_name_error = user_name_error, password_error = password_error, verify_password_error = verify_password_error, email = email, email_error = email_error)

@app.route("/")
def index():
    return render_template('index.html', user_name_error="", password_error="", verify_password_error="", email_error="", username = "", email = "")

app.run()

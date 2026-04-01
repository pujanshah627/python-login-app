from flask import Flask, render_template, request, redirect, url_for, session
import json
import os

app = Flask(__name__)
# Uses environment variable for security on live server,
# falls back to a default key for local development
app.secret_key = os.environ.get("SECRET_KEY", "pujan_local_dev_key_2024")

USERS_FILE = "users.json"

# Load users from file
def load_users():
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, "r") as f:
            return json.load(f)
    return {}

# Save users to file
def save_users(users):
    with open(USERS_FILE, "w") as f:
        json.dump(users, f)

@app.route("/")
def home():
    return redirect(url_for("login"))

@app.route("/register", methods=["GET", "POST"])
def register():
    message = ""
    if request.method == "POST":
        username = request.form["username"].strip()
        password = request.form["password"].strip()

        if not username or not password:
            message = "error:Please fill in all fields."
        else:
            users = load_users()
            if username in users:
                message = "error:Username already exists. Try a different one."
            else:
                users[username] = password
                save_users(users)
                message = "success:Account created successfully! You can now login."

    return render_template("register.html", message=message)

@app.route("/login", methods=["GET", "POST"])
def login():
    message = ""
    if request.method == "POST":
        username = request.form["username"].strip()
        password = request.form["password"].strip()

        if not username or not password:
            message = "error:Please fill in all fields."
        else:
            users = load_users()
            if username in users and users[username] == password:
                session["username"] = username
                return redirect(url_for("dashboard"))
            else:
                message = "error:Invalid username or password."

    return render_template("login.html", message=message)

@app.route("/dashboard")
def dashboard():
    if "username" not in session:
        return redirect(url_for("login"))
    return render_template("dashboard.html", username=session["username"])

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run()

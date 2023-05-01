from flask import Flask, redirect, url_for

app = Flask(__name__)

#Home page (landing)
@app.route("/") 
def home():
    return "Hello! <h1>HELLO<h1>"

#Just another page that displays the name of the id in the url
@app.route("/<name>/")
def anotherPage(name):
    return f"Hello {name}!"

#How to redirect back to any page
@app.route("/admin/")
def admin():
    #Must have name of function to redirect to
    #Can't pass "admin" to name as it will be stuck in a forever loop
    return redirect(url_for("anotherPage", name="admin!"))

if __name__ == "__main__":
    app.run()
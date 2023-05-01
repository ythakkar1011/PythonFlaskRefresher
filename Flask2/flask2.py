from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

#Home page (landing)
@app.route("/<name>") 
def home(name):
    #Using render_template to show my index.html page
    #This is how you can also show dynamic information
    return render_template("index.html", content=["Tim","Jake","Nate"])

if __name__ == "__main__":
    app.run()
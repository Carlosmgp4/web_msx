from flask import Flask, url_for, render_template,request, abort
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("inicio.html")



app.run("0.0.0.0",5000,debug=True)
from flask import Flask, url_for, render_template,request, abort
import json
app = Flask(__name__)

with open ("msx.json") as f:
    datos = json.load(f)

@app.route("/")
def index():
    return render_template("inicio.html")

@app.route("/juegos",methods=["GET","POST"])
def juegos():
    return render_template("juegos.html")

@app.route("/listajuegos",methods=["POST"])
def listajuegos():
    try:
        bus=request.form["nombrebus"]
    except:
        abort(404)

    nom = []
    desa = []
    id = []
    for w in datos:
        if bus == str(w.get("nombre"))[:len(bus)]:
            nom.append(w.get("nombre"))
            desa.append(w.get("desarrollador"))
            id.append(w.get("id"))

    return render_template("listajuegos.html",nombres=nom,desarrolladores=desa,id=id)

app.run("0.0.0.0",5000,debug=True)
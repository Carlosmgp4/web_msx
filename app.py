import os
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

    lista = []
    if bus:
        for w in datos:
            if bus == str(w.get("nombre"))[:len(bus)]:
                lista.append(w)
    else:
        for d in datos:
            lista.append(d)

    return render_template("listajuegos.html",lista=lista,busqueda=bus)

@app.route("/juego/<identificador>",methods=["GET","POST"])
def infojuegos(identificador):
    identificador=int(identificador)
    iden=[]
    lista=[]
    for i in datos:
        iden.append(i.get("id"))
    if identificador in iden:
        for var in datos:
            if var.get("id") == identificador:
                lista.append(var)
    else:
        abort(404)
    
    return render_template("detalles.html",lista=lista)

port=os.environ["PORT"]
app.run("0.0.0.0",int(port),debug=False)
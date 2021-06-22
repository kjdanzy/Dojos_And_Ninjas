from flask_app.controllers.ninjas import create_this_ninja
from flask import Flask, render_template, request, redirect

from flask_app import app
from flask_app.config.mysqlconnection import log_this
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja


@app.route("/dojos")
def index():
    dojos = Dojo.get_all_dojos()
    log_this("index route", dojos, "", "")
    return render_template("dojos.html", dojos = dojos)

@app.route("/get_dojo/<int:id>")
def get_dojo(id):
    data = {
        "id": id
    }
    
    dojo = Dojo.get_selected_dojo(data)
    
    log_this("index app route - dojos", dojo, data, "")

    return render_template("dojos_and_ninjas.html", dojo = dojo)
    

@app.route("/create_dojo", methods=["POST"])
def create_dojo():
    data = {
        "name" : request.form["name"]
    }
    Dojo.create_a_dojo(data)
    log_this("create dojo route", data, "", "")
    return redirect("/dojos")

@app.route("/create_new_ninja")
def create_new_ninja():
    dojos = []
    results = Dojo.get_all_dojos()
    for dojo in results:
        dojos.append(dojo)

    log_this("create ninja route", results, "", "")
    return render_template("new_ninja.html", dojos = dojos)

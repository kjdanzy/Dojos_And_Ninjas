from flask_app.config.mysqlconnection import log_this
from flask import Flask, render_template, request, redirect

from flask_app import app
from flask_app.models.ninja import Ninja


@app.route("/create_ninja", methods=["POST"])
def create_this_ninja():
    data = {
        "dojo_id" : request.form["my_dojo_id"],
        "first_name" : request.form["first_name"],
        "last_name" : request.form["last_name"],
        "age" : int(request.form["age"])
    }
    log_this("create_this_ninja - app route", data, "", "")
    dojo_id = data["dojo_id"]
    if (dojo_id == ''):
        dojo_id = 1
        
    log_this("create_this_ninja - app route", dojo_id, "", "")
    Ninja.create_this_ninja(data)
    return redirect("/get_dojo/" + str(dojo_id) )





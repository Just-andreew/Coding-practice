from flask import Blueprint, redirect, render_template

helloworld_bp  = Blueprint("helloworld", __name__, template_folder="templates")

@helloworld_bp.route("/")
def index():
    return "Hello World"

@helloworld_bp.route("/hello")
def hello():
    return "Hello World Again!"

@helloworld_bp.route("/hello/<name>")
def hello_name(name):
    return f"Hello {name}!"

@helloworld_bp.route("/hellohtml")
def html_hello():
    return render_template("hello.html")
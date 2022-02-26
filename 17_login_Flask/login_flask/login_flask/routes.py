from flask import render_template, request
from login_flask.login_flask import app, db
from login_flask.login_flask.models import Usuarios

@app.route('/')
def index():
    template_name = 'index.html'
    usuarios = Usuarios.query.all()
    return render_template(template_name, usuarios = usuarios)
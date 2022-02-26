from login_flask.login_flask.config import db

class Usuarios(db.Model):
    cod_usuario = db.Column(db.String(4), primary_key = True)
    username = db.Column(db.String(20))
    email = db.Column(db.String(20))
    password = db.Column(db.String(8))

#constructor cuando se desea pasar valores al servicio
    def __init__(self, cod_usuario, username, email, password):
        self.cod_usuario = cod_usuario
        self.username = username
        self.email = email
        self.password = password
        

#-----------------------------------------------------------------------------
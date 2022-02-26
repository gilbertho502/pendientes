from app import db

class Grupos(db.Model):
    codgrupo=db.Column(db.String(5),primary_key=True)#,autoincrement=True)
    nombre_grupo=db.Column(db.String(50))
    descripcion_grupo = db.Column(db.Text)
    estado=db.Column(db.Integer)

#constructor cuando se desea pasar valores al servicio
    def __init__(self, nombre_grupo, descripcion_grupo, estado):
        self.nombre_grupo = nombre_grupo
        self.descripcion_grupo = descripcion_grupo
        self.estado = estado
        

#-----------------------------------------------------------------------------

class Alumnos(db.Model):
    codalu = db.Column(db.String(5), primary_key = True )
    nombre_alumno = db.Column(db.String(50))
    apellido_alumno = db.Column(db.String(50))
    edad_alumno = db.Column(db.Integer)
    fechanac_alumno = db.Column(db.Date)
    ciudad = db.Column(db.String(50))
    estado = db.Column(db.Integer)
    codgrupo = db.Column(db.String(5), db.ForeignKey("Grupos.codgrupo"))

    def __init__(self, codalu, nombre_alumno, apellido_alumno, edad_alumno, fechanac_alumno, ciudad, estado, codgrupo):
        self.cadalu = codalu
        self.nombre_alumno = nombre_alumno
        self.apellido_alumno = apellido_alumno
        self.edad_alumno = edad_alumno
        self.fechanac_alumno = fechanac_alumno
        self.ciudad = ciudad
        self.estado = estado
        self.codgrupo = codgrupo
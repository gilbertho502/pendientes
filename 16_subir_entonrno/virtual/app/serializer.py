from app import app

from app.models import Grupos, Alumnos
#todo la libreria marshmallow me permite serializar
#todo los objetos de mi clase a un formato json
from flask_marshmallow import Marshmallow

ma= Marshmallow(app)

class GrupoSerializer(ma.SQLAlchemyAutoSchema):
    class Meta:
        model=Grupos
        fields=('codgrupo','nombre_grupo','descripcion_grupo','estado')


class AlumnoSerializer(ma.SQLAlchemyAutoSchema):
    class Meta:
        model= Alumnos
        fields = ('codalu', 'nombre_alumno', 'apellido_alumno', 'edad_alumno', 'fechanac_alumno', 'ciudad', 'estado', 'codgrupo')

#todo lo utilizare cuando deseo mostrar solo un registro        
grupo_schema=GrupoSerializer()
#todo lo utilizare cuando deseo mostrar varios
grupos_schema=GrupoSerializer(many=True)

alumno_schema = AlumnoSerializer()
alumnos_schema = AlumnoSerializer(many = True)
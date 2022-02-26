from app_tienda import db

    
class users(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    user_name=db.Column(db.String(15))
    password=db.Column(db.String(25))
    first_name=db.Column(db.String(15))
    last_name=db.Column(db.String(15))
    phone_number=db.Column(db.String(20))
    mail = db.Column(db.String(100))
    photo_user = db.Column(db.String(120))
    
class product_category(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(23))
    description=db.Column(db.String(250))
    items = db.relationship('products', backref='product_category', lazy='dynamic')
                            # tabla hija            tabla padre             tipo de ralacion    
class products(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(50))
    description=db.Column(db.Text)    
    stock_code=db.Column(db.String(13))
    category_id=db.Column(db.Integer,db.ForeignKey('product_category.id'))
    inventory_id=db.Column(db.Integer)
    price=db.Column(db.Float)
    discount_id=db.Column(db.Integer)
    
    
    
    
 
        
    
#create SEQUENCE usuarios_id_seq;
#alter table usuarios alter column cod_usuario set default 
#nextval('usuarios_id_seq'::regclass)    
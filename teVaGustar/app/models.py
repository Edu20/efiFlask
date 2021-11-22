import datetime
from flask import url_for
from slugify import slugify
from sqlalchemy.exc import IntegrityError

from app import db


# class Comment(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('blog_user.id', ondelete='SET NULL'))
#     user_name = db.Column(db.String(256))
#     post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)
#     content = db.Column(db.Text)
#     created = db.Column(db.DateTime, default=datetime.datetime.utcnow)

#     def __init__(self, content, user_id=None, user_name=user_name, post_id=None):
#         self.content = content
#         self.user_id = user_id
#         self.user_name = user_name
#         self.post_id = post_id

#     def __repr__(self):
#         return f'<Comment {self.content}>'

#     def save(self):
#         if not self.id:
#             db.session.add(self)
#         db.session.commit()

#     def delete(self):
#         db.session.delete(self)
#         db.session.commit()

#     @staticmethod
#     def get_by_post_id(post_id):
#         return Comment.query.filter_by(post_id=post_id).all()







class Product(db.Model):
    __tablename__ = 'productos'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(256), nullable=False)
    descripcion = db.Column(db.String(256), nullable=False)

    
    
    def __init__(self, nombre=nombre, descripcion=descripcion):
        self.nombre = nombre
        self.descripcion = descripcion
        
    
    def __repr__(self):
        return f'<Product {self.nombre}>'

    def save(self):
        db.session.add(self)



    def get_product(self):
        return db.session.query(self).all()

    def delete (self):
        db.session.delete(self)
        db.session.commit

    @staticmethod
    def get_by_descripcion(descripcion):
        return Product.query.filter_by(descripcion=descripcion).first()

    @staticmethod
    def get_by_id(id):
        products = db.session.query(Product,Category).join(Category, Category.id == Product.categoria_id
        ).filter(Product.categoria_id == id
        ).all()
       
        return products

    @staticmethod
    def get_all():
    
        return Product.query.all()


class Talle(db.Model):
    __tablename__ = 'talles'
    id = db.Column(db.Integer, primary_key=True)
    talles = db.Column(db.String(256), nullable=False)

    def __init__(self, talles=talles):
        self.talles = talles


class Color(db.Model):
    __tablename__ = 'color'
    id = db.Column(db.Integer, primary_key=True)
    colores = db.Column(db.String(256), nullable=False)

    def __init__(self, colores=colores):
        self.colores = colores

class Category(db.Model):
    __tablename__ = 'categoria'
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(256), nullable=False)
    imagen = db.Column(db.String(250), nullable=False)
    
    def __init__(self,category=category,imagen=imagen):
        self.category = category
        self.imagen = imagen
    def get_all():
        return Category.query.all()



class DetalleProducto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    producto_id = db.Column(db.Integer, db.ForeignKey('productos.id', ondelete = 'SET NULL'))
    categoria_id = db.Column(db.Integer, db.ForeignKey('categoria.id', ondelete = 'SET NULL'))
    color_id = db.Column(db.Integer, db.ForeignKey('color.id', ondelete = 'SET NULL'))
    talle_id = db.Column(db.Integer, db.ForeignKey('talles.id', ondelete = 'SET NULL'))
    imagen_name = db.Column(db.String(250), nullable=False)
    cantidad = db.Column(db.Integer)

    def __init__(self, producto_id=producto_id, categoria_id=categoria_id, color_id=color_id, talle_id=talle_id, imagen_name=imagen_name, cantidad=cantidad):
        self.producto_id = producto_id
        self.categoria_id = categoria_id
        self.color_id = color_id
        self.talle_id = talle_id
        self.imagen_name = imagen_name
        self.cantidad = cantidad

    def get_by_category(self, idCategoria):
        return db.session.query(DetalleProducto).filter(DetalleProducto.categoria_id==idCategoria).all()
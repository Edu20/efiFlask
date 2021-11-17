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







class Products(db.Model):
    __tablename__ = 'productos'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(256), nullable=False)
    descripcion = db.Column(db.String(256), nullable=False)
    imagen = db.Column(db.String(20), nullable=False)


class Talle(db.Model):
    __tablename__ = 'talles'
    id = db.Column(db.Integer, primary_key=True)
    talles = db.Column(db.String(256), nullable=False)


class Color(db.Model):
    __tablename__ = 'color'
    id = db.Column(db.Integer, primary_key=True)
    colores = db.Column(db.String(256), nullable=False)

class Category(db.Model):
    __tablename__ = 'categoria'
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(256), nullable=False)

class DetalleProducto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    producto_id = db.Column(db.Integer, db.ForeignKey('productos.id', ondelete = 'SET NULL'))
    categoria_id = db.Column(db.Integer, db.ForeignKey('categoria.id', ondelete = 'SET NULL'))
    color_id = db.Column(db.Integer, db.ForeignKey('color.id', ondelete = 'SET NULL'))
    talle_id = db.Column(db.Integer, db.ForeignKey('talles.id', ondelete = 'SET NULL'))
    imagen_name = db.Column(db.String(20), nullable=False)
    cantidad = db.Column(db.Integer)

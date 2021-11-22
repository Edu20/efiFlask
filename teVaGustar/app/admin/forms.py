# HEREDAMOS FLASKFORM
from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
# HEREDAMOS 4 COMPONENTES, CAJA DE TEXTO, BOTON SUBMIT, CAMPO PARA CLAVE y AREA DE TEXTO
from wtforms import StringField, SubmitField, TextAreaField, BooleanField
from wtforms.fields.core import SelectField
from wtforms.fields.simple import FileField
# HEREDAMOS VALIDADORES, DATO REQUERIDO, EMAIL Y LARGO DE UN CAMPO
from wtforms.validators import DataRequired, Length




class ProductForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired(), Length(max=128)])
    descripcion = TextAreaField('Descripcion')
    imagen = FileField('Imagen de producto',validators=[
        FileAllowed(['jpg','png', 'solo se permiten imágenes'])
    ])
    submit = SubmitField('Guardar')
  

class CategoryForm(FlaskForm):
    category = StringField('Category', validators=[DataRequired(), Length(max=128)])
    imagen = FileField('Category', validators=[DataRequired()])
    submit = SubmitField('Guardar')

class ColorForm(FlaskForm):
    color = StringField('Color', validators=[DataRequired(), Length(max=128)])
    submit = SubmitField('Guardar')

class TalleForm(FlaskForm):
    talle = StringField('talle', validators=[DataRequired(), Length(max=128)])
    submit = SubmitField('Guardar')


class DetalleProductoForm(FlaskForm):
    producto_id = SelectField('producto', choices=['dfdf','hola'])
    submit = SubmitField('Guardar')
    

        
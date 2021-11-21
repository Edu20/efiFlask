from flask import render_template, redirect, url_for, abort, request,current_app
from werkzeug.utils import secure_filename

from flask_login import login_required, current_user
from app.auth.decorators import admin_required
from app.auth.models import User
from app.models import Product, Category, Color, Talle, DetalleProducto
from app.admin.forms import ProductForm, CategoryForm, ColorForm, TalleForm, DetalleProductoForm
from . import admin_bp
from app import db
import os 
##from .forms import PostForm, UserAdminForm

@admin_bp.route("/admin/")
@login_required
@admin_required
def index():
    print('"entta aca>??????????')
    return render_template("admin/index.html")

@admin_bp.route("/admin/categories/", methods=['GET', 'POST'])
@login_required
@admin_required
def add_Category():
    form = CategoryForm()
    if form.validate_on_submit():
        
        categoryName = form.category.data
        category = Category(categoryName)
        db.session.add(category)
        db.session.commit()
        
        return redirect(url_for('admin.list_posts'))

    return render_template("admin/newcategory.html",form=form)


@admin_bp.route("/admin/talles/", methods=['GET', 'POST'])
@login_required
@admin_required
def add_Talle():
    form = TalleForm()
    if form.validate_on_submit():
        
        talleName = form.talle.data
        talle = Talle(talleName)
        db.session.add(talle)
        db.session.commit()
        
        return redirect(url_for('admin.list_posts'))

    return render_template("admin/talle_form.html",form=form)


@admin_bp.route("/admin/detalleProducto/", methods=['GET', 'POST'])
@login_required
@admin_required
def add_DetalleProducto():
    productos = db.session.query(Product).all()
    talles = db.session.query(Talle).all()
    categorias = db.session.query(Category).all()
    colores = db.session.query(Color).all()
    

    return render_template("admin/detalleProducto.html",productos=productos,talles=talles, categorias=categorias, colores=colores)


@admin_bp.route("/admin/colores/", methods=['GET', 'POST'])
@login_required
@admin_required
def add_Color():
    form = ColorForm()
    if form.validate_on_submit():
        
        colorName = form.color.data
        color = Color(colorName)
        db.session.add(color)
        db.session.commit()
        
        return redirect(url_for('admin.list_posts'))

    return render_template("admin/color_form.html",form=form)

@admin_bp.route("/admin/posts/")
@login_required
@admin_required
def list_posts():
    posts = "222222"
    return render_template("admin/posts.html", posts=posts)

@admin_bp.route("/admin/add_Product/", methods=['GET', 'POST'])
@login_required
@admin_required
def add_Product():
    #   Crea un nuevo post   #
    form = ProductForm()
    if form.validate_on_submit():
        nombre = form.nombre.data
        descripcion = form.descripcion.data
        imagen = form.imagen.data
        product = Product(nombre, descripcion, imagen)
        db.session.add(product)
        db.session.commit()
        return redirect(url_for('admin.list_posts'))
    return render_template("admin/product_form.html", form=form)

@admin_bp.route("/admin/save_product/", methods=['POST'])
@login_required
@admin_required
def add_DetalleProduct():
    if request.method == 'POST':
        producto = request.form['producto']
        categoria = request.form['categoria']
        color = request.form['color']
        talle = request.form['talle']
        imagen = request.files['imagen']
        cantidad = request.form['cantidad']
        print(imagen.filename)
        if imagen:
            file_path = current_app.config['UPLOAD_FOLDER']
            image_name = secure_filename(imagen.filename)

            imagen.save(os.path.join(current_app.config["UPLOAD_FOLDER"],image_name))

        detalle = DetalleProducto(producto,categoria,color,talle,'./teVaGustar/app/uploads/'+image_name,cantidad)
        db.session.add(detalle)
        db.session.commit()
        return render_template('admin/index.html')


@admin_bp.route("/admin/post/<int:post_id>/", methods=['GET', 'POST'])
@login_required
@admin_required
def update_post_form(post_id):
  
    return render_template("admin/post_form.html")

# @admin_bp.route("/admin/post/delete/<int:post_id>/", methods=['POST', ])
# @login_required
# @admin_required
# def delete_post(post_id):
#     post = Post.get_by_id(post_id)
#     if post is None:
#         abort(404)
#     post.delete()
#     return redirect(url_for('admin.list_posts'))

# @admin_bp.route("/admin/user/<int:user_id>/", methods=['GET', 'POST'])
# @login_required
# @admin_required
# def update_user_form(user_id):
#     # Acá entra para actualizar un usuario existente
#     user = User.get_by_id(user_id)
#     if user is None:
#         abort(404)
#     # Crea un formulario inicializando los campos con los valores del usuario.
#     form = UserAdminForm(obj=user)
#     if form.validate_on_submit():
#         # Actualiza los campos del usuario existente
#         user.is_admin = form.is_admin.data
#         user.save()
#         return redirect(url_for('admin.list_users'))
#     return render_template("admin/user_form.html", form=form, user=user)

# @admin_bp.route("/admin/user/delete/<int:user_id>/", methods=['POST', ])
# @login_required
# @admin_required
# def delete_user(user_id):
#     user = User.get_by_id(user_id)
#     if user is None:
#         abort(404)
#     user.delete()
#     return redirect(url_for('admin.list_users'))

# @admin_bp.route("/admin/users/")
# @login_required
# @admin_required
# def list_users():
#     users = User.get_all()
#     return render_template("admin/users.html", users=users)
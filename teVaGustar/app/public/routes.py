from flask import abort, render_template, redirect, url_for, request
from flask_login import current_user

from app.models import Product, Category
from . import public_bp
from .forms import CommentForm

@public_bp.route("/")
def index():
    categories = Category.get_all()
    return render_template("public/index.html",categories=categories)

# Un slug es una cadena de caracteres alfanuméricos (más el carácter ‘-‘)
# sin espacios, tildes ni signos de puntuación
@public_bp.route("/p/<string:descripcion>/", methods=['GET', 'POST'])
def show_products(descripcion):
    product = Product.get_by_descripcion(descripcion)
    if not product:
        abort(404)
    # form = CommentForm()
    # if current_user.is_authenticated and form.validate_on_submit():
    #     content = form.content.data
    #     comment = Comment(content=content, user_id=current_user.id, user_name=current_user.name, post_id=post.id)
    #     comment.save()
    #     return redirect(url_for('public.show_post', slug=post.title_slug))
    return render_template("public/product_view.html", product=product, form=form)

@public_bp.route("/error")
def show_error():
    res = 1 / 0
    products = Product.get_all()
    return render_template("public/index.html", products=products)




@public_bp.route("/viewcategory/<idCategory>", methods=['GET'])
def getProductByCategory(idCategory):
    if request.method == 'GET':
        productos = Product.get_by_id(idCategory)
        return render_template("public/productsByCategory.html",productos=productos)    
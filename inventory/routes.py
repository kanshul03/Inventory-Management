from flask import  render_template,url_for,redirect,flash,request
from inventory import app,db
from inventory.forms import addproduct,editproduct
from inventory.models import Product
from sqlalchemy.exc import IntegrityError


@app.route("/", methods = ['GET','POST'])
@app.route("/Product", methods = ['GET','POST'])
def product():
    form = addproduct()
    eform = editproduct()
    details = Product.query.order_by(Product.prod_name).all()
    exists = bool(Product.query.order_by(Product.prod_name).all())
    if exists== False and request.method == 'GET' :
            flash(f'Add products to view','info')
    elif eform.validate_on_submit() and request.method == 'POST':
        pname = request.form.get("productname","")
        details = Product.query.order_by(Product.prod_name).all()
        prod = Product.query.filter_by(prod_name = pname).first()
        prod.prod_name = eform.editname.data
        prod.prod_qty = eform.editqty.data
        prod.prod_price = eform.editprice.data
        try:
            db.session.commit()
            flash(f'Your product  has been updated!', 'success')
            return redirect('/Product')
        except IntegrityError :
            db.session.rollback()
            flash(f'This product already exists','danger')
            return redirect('/Product')
        return render_template('product.html',details=details,eform=eform)

    elif form.validate_on_submit() :
        product = Product(prod_name=form.prodname.data,prod_qty=form.prodqty.data,prod_price=form.prodprice.data)
        db.session.add(product)
        try:
            db.session.commit()
            flash(f'Your product {form.prodname.data} has been added!', 'success')
            return redirect(url_for('product'))
        except IntegrityError :
            db.session.rollback()
            flash(f'This product already exists','danger')
            return redirect('/Product')
    return render_template('product.html',eform=eform,form = form,details=details)




@app.route("/delete")
def delete():
    pname = request.args.get('pname')
    product = Product.query.filter_by(prod_name=pname).delete()
    db.session.commit()
    flash(f'Product deleted!', 'success')
    return redirect(url_for('product'))
    return render_template('product.html')

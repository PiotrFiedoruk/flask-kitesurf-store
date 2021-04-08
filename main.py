from flask import Flask, request, render_template, make_response, redirect
from database_queries import dis_category, dis_brand, dis_product, dis_product_all, dis_product_one, add_product

app = Flask(__name__)

@app.route('/')
def main():
    brands = dis_brand()
    categories = dis_category()
    products = dis_product()
    return render_template("main.html", category=categories, brand=brands, product=products)

@app.route('/brand/<brand>', methods=['GET', 'POST'])
def brand(brand):
    brands = dis_brand()
    categories = dis_category()
    brand_products = dis_product_all('brand', brand)
    filter_by_category = list(set([y['category'] for y in brand_products]))
    filter_by_year = list(set([y['year'] for y in brand_products]))
    filter_by_model = list(set([y['model'] for y in brand_products]))
    return render_template("brand.html", brand=brands, category=categories, cur_brand=brand, products=brand_products,
                           f_category=filter_by_category, f_year=filter_by_year, f_model=filter_by_model)

@app.route('/category/<category>', methods=['GET', 'POST'])
def category(category):
    brands = dis_brand()
    categories = dis_category()
    category_products = dis_product_all('category', category)
    # filter products by brand:
    filter_by_brand = list(set([y['brand'] for y in category_products]))
    filter_by_year = list(set([y['year'] for y in category_products]))
    filter_by_model = list(set([y['model'] for y in category_products]))
    return render_template("category.html", brand=brands, category=categories, cur_category=category, 
                                products=category_products, f_brand=filter_by_brand, f_year=filter_by_year, 
                                f_model=filter_by_model)

@app.route('/product/<product>')
def product(product):
    brands = dis_brand()
    categories = dis_category()
    cur_product = dis_product_one('id', product)
    similar_products = dis_product_all('category', cur_product['category'])
    return render_template("product.html", brand=brands, category=categories, product=cur_product, similar_products=similar_products)



@app.route('/backend')
def backend():
    brands = dis_brand()
    categories = dis_category()
    return render_template("backend.html", brand=brands, category=categories, product=product)

@app.route('/test')
def test():
    brands = dis_brand()
    categories = dis_category()
    return render_template("test.html", brand=brands, category=categories, product=product)

@app.route('/admin')
def admin():
    brands = dis_brand()
    categories = dis_category()
    products = dis_product_all('name', '%')
    return render_template("admin.html", brand=brands, category=categories, products=products)

@app.route('/admin/addproduct', methods=['GET', 'POST'])
def admin_add_product():
    if request.method == 'POST':
        add_product(**request.form)
    brands = dis_brand()
    categories = dis_category()
    products = dis_product_all('name', '%')
    return render_template("admin_add_product.html", brand=brands, category=categories, products=products)

@app.route('/setcookie', methods=['POST', 'GET'])
def setcookie():
    if request.method == 'POST':
        product_id = request.form['product_id']
        quantity = request.form['quantity']
        cookie_dict = product_id
        resp = make_response(redirect(f'/product/{product_id}'))
        resp.set_cookie('Basket', value=cookie_dict)
        return resp

@app.route('/basket')
def basket():
    product_cookie = request.cookies.get('Basket')
    # quantity = request.cookies.get('Basket')
    basket_product = dis_product_one('id', product_cookie)
    brands = dis_brand()
    categories = dis_category()
    return render_template("basket.html", brand=brands, category=categories, product_id=product_cookie, b_product=basket_product)

if __name__ == '__main__':
    app.run()

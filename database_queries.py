from connection import connect
from psycopg2 import extras


# def add_category(category):
#     sql_add_category = f"""
#     INSERT INTO category (name) values ('{category}');
#     """
#     conn = connect()
#     cursor = conn.cursor()
#     cursor.execute(sql_add_category)
#     conn.close()

def dis_category(category='%'):
    sql_dis_category = f"""
    SELECT DISTINCT category FROM product;
    """
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(sql_dis_category)
    data = cursor.fetchall()
    unpack_data = [category[0].title() for category in data]
    conn.close()
    return unpack_data

# def add_brand(brand):
#     sql_add_brand = f"""
#     INSERT INTO brands (name) values ('{brand}');
#     """
#     conn = connect()
#     cursor = conn.cursor()
#     cursor.execute(sql_add_brand)
#     conn.close()


def dis_brand(brand='%'):
    sql_dis_brand = f"""
    SELECT DISTINCT brand FROM product;
    """
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(sql_dis_brand)
    data = cursor.fetchall()
    unpack_data = [brand[0].title() for brand in data]
    conn.close()
    return unpack_data


def add_product(name, brand, category, model, year, size, description, price, active, width, length, weight, movie_link, technologies, stock):
    sql_add_brand = f"""
    INSERT INTO product (name, brand, category, model, year, size, description, price, active, width, length, weight, movie_link, technologies, stock ) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
    """
    values = (name, brand, category, model, year, size, description, price, active, width, length, weight, movie_link, technologies, stock)
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(sql_add_brand, values)
    conn.close()

def dis_product(product ='%'):
    sql_dis_product = f"""
    SELECT * FROM product WHERE name LIKE '{ product }';
    """
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(sql_dis_product)
    data = cursor.fetchall()
    # unpack_data = (product for product in data)
    conn.close()
    return data

# def dis_product_by_id(id ='%'):
#     sql_dis_product_by_id = f"""
#     SELECT * FROM product WHERE id = '{ id }';
#     """
#     conn = connect()
#     cursor = conn.cursor()
#     cursor.execute(sql_dis_product_by_id)
#     data = cursor.fetchone()
#     # unpack_data = (product for product in data)
#     conn.close()
#     return data

# def dis_product_by_category(category ='%'):
#     sql_dis_product_by_category = f"""
#     SELECT * FROM product WHERE p_category = '{ category }';
#     """
#     conn = connect()
#     cursor = conn.cursor()
#     cursor.execute(sql_dis_product_by_category)
#     data = cursor.fetchall()
#     # unpack_data = (product for product in data)
#     conn.close()
#     return data

# def dis_product_by_brand(brand ='%'):
#     sql_dis_product_by_brand = f"""
#     SELECT * FROM product WHERE brand = '{ brand }';
#     """
#     conn = connect()
#     cursor = conn.cursor()
#     cursor.execute(sql_dis_product_by_brand)
#     data = cursor.fetchall()
#     # unpack_data = (product for product in data)
#     conn.close()
#     return data


def dis_product_all(column='%', value='%'):
    sql_dis_product = f"""
    SELECT * FROM product WHERE { column } LIKE '{ value }';
    """
    conn = connect()
    cursor = conn.cursor(cursor_factory=extras.DictCursor)
    cursor.execute(sql_dis_product)
    data = cursor.fetchall()
    conn.close()
    return data

def dis_product_one(column='%', value='%'):
    sql_dis_product = f"""
    SELECT * FROM product WHERE { column } = '{ value }';
    """
    conn = connect()
    cursor = conn.cursor(cursor_factory=extras.DictCursor)
    cursor.execute(sql_dis_product)
    data = cursor.fetchone()
    conn.close()
    return data

#
# y = dis_brand()
# print(y)
#
# z = dis_brand()
# print(z)

# category_products = dis_product_all('category', 'Kites')
# print(category_products)

# e = [y['brand'] for y in category_products]
# filter_by_brand = list(set([y['brand'] for y in category_products]))



# products = dis_product_one('id', 1)
# similar_products = dis_product_all('name', '%')
#
#
# print(similar_products)

# for i in range(0,4):
#     print(similar_products[i]['name'], )

# x = dis_product_all('p_category', 'Kites')
# for i in range(0,len(x)):
#     print(x[i]['name'])
# print(x[0]['brand'])

#

# x = dis_product_by_category('Kites')
# print(x)

# print(x[0][1])

# add_product('Stretch', 'Duotone', 'Leashes', 'Stretch', '2020', '152cm', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc dapibus felis at venenatis suscipit. Proin porta in justo ac fermentum. Pellentesque cursus neque ut tristique laoreet. Pellentesque accumsan ut libero eget pretium. Sed sed ipsum imperdiet, imperdiet mi eget, feugiat nisl. Nullam tincidunt aliquet nisl aliquet vulputate. Integer sed ipsum sit amet dui convallis placerat. Donec at nunc bibendum velit gravida vehicula. Sed ut nibh ac lorem rhoncus aliquet. Cras lorem est, bibendum non quam sed, vehicula placerat purus. Vivamus venenatis tellus et blandit feugiat. Vestibulum efficitur, augue imperdiet condimentum hendrerit, nulla urna cursus ipsum, at maximus nibh diam vel urna.', 1200.00, 'True' )
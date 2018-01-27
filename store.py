from bottle import route, run, template, static_file, get, post, delete, request
from sys import argv
import json
import pymysql

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='1q2w3e4r',
                             db='store2',
                             cursorclass=pymysql.cursors.DictCursor)


@get("/admin")
def admin_portal():
	return template("pages/admin.html")


@get("/")
def index():
    return template("index.html")


@get('/js/<filename:re:.*\.js>')
def javascripts(filename):
    return static_file(filename, root='js')


@get('/css/<filename:re:.*\.css>')
def stylesheets(filename):
    return static_file(filename, root='css')


@get('/images/<filename:re:.*\.(jpg|png|gif|ico)>')
def images(filename):
    return static_file(filename, root='images')


@post("/category")
def create_category():
    name = request.POST.get('name')
    if not name:
        return json.dumps({"STATUS": "ERROR", "MSG": "Name parameter is missing", "CODE": "400 - Bad request"})
    else:
        try:
            with connection.cursor() as cursor:
                sql = "select name from categories where name = '{}'".format(name)
                cursor.execute(sql)
                result = cursor.fetchone()
                if result == None:
                    sql = "INSERT INTO categories(name) VALUES ('{}'); ".format(name)
                    cursor.execute(sql)
                    connection.commit()
                    result = cursor.lastrowid
                    return json.dumps({"STATUS": "SUCCESS", "CAT_ID": result, "CODE": "201 - category created successfully"})
                else:
                    return json.dumps({"STATUS": "ERROR", "MSG": "Category already exists","CODE": "200 - category already exists"})
        except Exception as e:
            return json.dumps({"STATUS": "ERROR", "MSG": "Internal error", "CODE": "500 - Internal error"})


@delete("/category/<id>")
def delete_category(id):
    try:
        with connection.cursor() as cursor:
            sql = "select id from categories where id = '{}'".format(id)
            cursor.execute(sql)
            result = cursor.fetchone()
            if result == None:
                return json.dumps({"STATUS": "ERROR", "MSG": "Category not found", "CODE": "404 - Category not found"})
            else:
                sql = """DELETE FROM categories
                         WHERE id = '{}'""".format(id)
                cursor.execute(sql)
                connection.commit()
                return json.dumps({"STATUS": "SUCCESS", "CODE": "201 - Category deleted successfully"})
    except Exception as e:
        return json.dumps({"STATUS": "ERROR", "MSG": "Internal error", "CODE": "500 - Internal error"})


@get("/categories")
def list_of_categories():
    try:
        with connection.cursor() as cursor:
            sql = "select * from categories;"
            cursor.execute(sql)
            result = cursor.fetchall()
        return json.dumps({"STATUS": "SUCCESS", "CATEGORIES": result, "CODE": "200 - Success"})
    except Exception as e:
        return json.dumps({"STATUS": "ERROR", "MSG": "Internal error", "CODE": "500 - Internal error"})


@post("/product")
def add_and_edit_product(products{}):
    try:
        return json.dumps({"STATUS": "SUCCESS", "PRODUCT_ID":,"CODE": "201 - Product created/updated  successfully"})
    except:
    #elif code = 400
        return json.dumps({"STATUS": "ERROR", "MSG": "Missing parameters","CODE": "400 - Bad request"})
    # elif code = 404:
        return json.dumps({"STATUS": "ERROR", "MSG": "Category not found","CODE": "404 - Category not found"})
    # elif code = 500:
        return json.dumps({"STATUS": "ERROR", "MSG": "Internal error","CODE": "500 - Internal error"})


@get("/product/<id>")
def get_product(id):
    try:
        with connection.cursor() as cursor:
            sql = "select id from products where id = '{}'".format(id)
            cursor.execute(sql)
            result = cursor.fetchone()
            if result == None:
                return json.dumps({"STATUS": "ERROR", "MSG": "Product not found", "CODE": "404 - Product not found"})
            else:
                sql = """DELETE FROM products
                            WHERE id = '{}'""".format(id)
                cursor.execute(sql)
                connection.commit()
                return json.dumps(
                    {"STATUS": "SUCCESS", "PRODUCT": result, "CODE": "200 - Product fetched successfully"})
    except Exception as e:
        return json.dumps({"STATUS": "ERROR", "MSG": "Internal error", "CODE": "500 - Internal error"})


@delete("/product/<id>")
def delete_product(id):
    try:
        with connection.cursor() as cursor:
            sql = "select id from products where id = '{}'".format(id)
            cursor.execute(sql)
            result = cursor.fetchone()
            if result == None:
                return json.dumps({"STATUS": "ERROR", "MSG": "Product not found", "CODE": "404 - Product not found"})
            else:
                sql = """DELETE FROM products
                         WHERE id = '{}'""".format(id)
                cursor.execute(sql)
                connection.commit()
                return json.dumps({"STATUS": "SUCCESS", "CODE": "201 - Product deleted successfully"})
    except Exception as e:
        return json.dumps({"STATUS": "ERROR", "MSG": "Internal error", "CODE": "500 - Internal error"})


@get("/products")
def list_of_products():
    try:
        with connection.cursor() as cursor:
            sql = "select * from products;"
            cursor.execute(sql)
            result = cursor.fetchall()
        return json.dumps({"STATUS": "SUCCESS", "PRODUCTS": result, "CODE": "200 - Success"})
    except:
        return json.dumps({"STATUS": "ERROR", "MSG": "Internal error", "CODE": "500 - Internal error"})


@get("/category/<id>/products")
def list_of_products_by_categories(id):
    try:
        with connection.cursor() as cursor:
            sql = "select * from products where category = '{}'".format(id)
            cursor.execute(sql)
            result = cursor.fetchall()
        return json.dumps({"STATUS": "SUCCESS", "PRODUCTS": result, "CODE": "200 - Success"})
    except:
        return json.dumps({"STATUS": "ERROR", "MSG": "Internal error", "CODE": "500 - Internal error"})



def main():
    run(host='localhost', port=7010)


if __name__ == '__main__':
    main()
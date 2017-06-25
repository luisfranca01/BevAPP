from flask import Flask, request, render_template, redirect, url_for, jsonify, flash,session, abort, Response
import os
import sqlite3
import json
from werkzeug import secure_filename

app = Flask(__name__)

db_database = os.path.join(os.path.dirname(os.path.abspath(__file__)), "database.db")

def createDir():
    if not os.path.exists("jpg_files"):
        os.makedirs("jpg_files")
    if not os.path.exists("pdf_files"):
        os.makedirs("pdf_files")

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

@app.route('/')
def index():
  return render_template('page.html')

@app.route('/apagarRow', methods=['POST', 'GET'])
def apagarRow():
    ident = str(request.form["string"])
    print(ident)
    with sqlite3.connect(db_database) as db:
        cursor = db.cursor()
        cursor.execute("delete from materiaprima where sql_id=(?);",(ident,))
        db.commit()
        return ""


@app.route('/editarmateriaprima', methods=['POST', 'GET'])
def editarmateriaprima():
    ident = str(request.form["id"])
    materiaprima = str(request.form["materiaprima"])
    sg20 = str(request.form["sg20"])
    abv = str(request.form["abv"])
    peg = str(request.form["peg"])
    brix = str(request.form["brix"])
    stock = str(request.form["stock"])
    unidade = str(request.form["unidade"])
    preco = str(request.form["preco"])
    lote = str(request.form["lote"])
    validade = str(request.form["validade"])
    with sqlite3.connect(db_database) as db:
        cursor = db.cursor()
        cursor.execute("""update materiaprima set
                            sql_materiaprima = (?),
                            sql_sg20 = (?),
                            sql_abv = (?),
                            sql_peg = (?),
                            sql_brix = (?),
                            sql_stock = (?),
                            sql_unidade = (?),
                            sql_preco = (?),
                            sql_lote = (?),
                            sql_validade = (?) where sql_id=(?);""",(materiaprima,sg20,abv,peg,brix,stock,unidade,preco,lote,validade,ident,))
        db.commit()
        return ""

@app.route('/manageUpload', methods=['POST', 'GET'])
def manageUpload():
    print('ok')
    f = request.form['file']
    print (f,type(f))
    return ('success')




@app.route('/guardarComentario', methods=['POST', 'GET'])
def guardarComentario():
    text = str(request.form["text"])
    ident = str(request.form["id"])
    with sqlite3.connect(db_database) as db:
        cursor = db.cursor()
        cursor.execute("""update materiaprima set sql_observacao  = (?) where sql_id=(?);""",(text,ident,))
        db.commit()
        return " "

@app.route('/getTableMP', methods=['POST', 'GET'])
def getTableMP():
    with sqlite3.connect(db_database) as db:
        db.row_factory = dict_factory
        cursor = db.cursor()
        cursor.execute('''select * from materiaprima;''')
        result = cursor.fetchall()
        return Response(json.dumps(result),mimetype='application/json')

@app.route('/adicionarMateriaPrima', methods=['POST', 'GET'])
def adicionarMateriaPrima():
    materiaprima = str(request.form["materiaprima"])
    sg20 = str(request.form["sg20"])
    abv = str(request.form["abv"])
    peg = str(request.form["peg"])
    brix = str(request.form["brix"])
    stock = str(request.form["stock"])
    unidade = str(request.form["unidade"])
    preco = str(request.form["preco"])
    lote = str(request.form["lote"])
    validade = str(request.form["validade"])
    with sqlite3.connect(db_database) as db:
        cursor = db.cursor()
        cursor.execute('''INSERT into materiaprima (sql_materiaprima,sql_sg20,sql_abv,sql_peg,sql_brix,sql_stock,sql_unidade,sql_preco,sql_lote,sql_validade) values (?,?,?,?,?,?,?,?,?,?)''',
                       (materiaprima,sg20,abv,peg,brix,stock,unidade,preco,lote,validade,))
        db.commit()
        return ""

def createDatabaseMP():
        with sqlite3.connect(db_database) as db:
	        cursor = db.cursor()
	        cursor.execute('''create table if not exists materiaprima (
                        sql_id INTEGER PRIMARY KEY,
                        sql_materiaprima TEXT,
                        sql_sg20 TEXT,
                        sql_abv TEXT,
                        sql_peg TEXT,
                        sql_brix TEXT,
                        sql_stock TEXT,
                        sql_unidade TEXT,
                        sql_preco TEXT,
                        sql_lote TEXT,
                        sql_validade TIMESTAMP,
                        sql_observacao TEXT,
                        sql_pdf TEXT);''')
	        db.commit()

def createDatabaseBebidas():
        with sqlite3.connect(db_database) as db:
	        cursor = db.cursor()
	        cursor.execute('''create table if not exists bebidasGuardadas (
                        sql_id INTEGER PRIMARY KEY,
                        sql_nomeBebida TEXT,
                        sql_quantidade TEXT,
                        sql_unidade TEXT,
                        sql_observacao TEXT,
                        sql_jpg TEXT,
                        sql_pdf TEXT);''')
	        db.commit()



if __name__ == '__main__':
    createDir()
    createDatabaseMP()
    createDatabaseBebidas()
    app.run(host='0.0.0.0', debug=True, threaded=True)

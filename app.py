from flask import Flask, redirect, url_for
from flask import request, render_template
from flask_material import Material
from db import celulares

app = Flask(__name__)
Material(app)


@app.route('/')
def index():
    return redirect(url_for('inicio'))


@app.route('/inicio')
def inicio():
    return render_template('index.html', title='Inicio', phones=celulares)


@app.route('/phone/add', methods=['POST', 'GET'])
def add():
    if request.method == 'POST':

        new={

            'marca': request.form['marca'],
            'modelo': request.form['modelo'],
            'precio': request.form['precio']
        }
        celulares.append(new)

        return redirect(url_for('inicio'))
    return render_template('add.html', title="Agregar")


@app.route('/phone/update', methods=['GET', 'POST'])
def update():
    if request.method == 'POST':
        row = [l for l in celulares if l['marca'] == request.form['marca']]

        if len(row) == 0:
            return render_template('update.html', title="Actualizar")

        row[0]['modelo'] = request.form['modelo']
        row[0]['precio'] = request.form['precio']

        return redirect(url_for('inicio'))

    return render_template('update.html', title='Actualizar')


@app.route('/phone/delete', methods=['POST', 'GET'])
def delete():
    if request.method == 'POST':
        row = [l for l in celulares if l['modelo'] == request.form['modelo']]
        if len(row) == 0:
            return "No se encontró el telefono"
        celulares.remove(row[0])
        return redirect(url_for('inicio'))

    return render_template('delete.html', title="Eliminar")

from flask import Flask, render_template, redirect, url_for
app = Flask(__name__)

# ruta  1


@app.route('/')
def hola_mundo():
    return "<h1> Bienvenido a Flask EMerson 2 3 2 1  </h1>"

# ruta 2


@app.route('/contacto')
def contacto():
    return "<h1> Escribe tu Contacto </h1>"

# rutas con variables string


@app.route('/contacto/<nombre>')
def saludo(nombre):
    return f'<h1> Bienvenido: {nombre.upper()} </h1> '

# rutas con variables enteros


@app.route('/edad/<int:edad>')
def edades(edad):
    return f'<h1> Tu edad es: {edad} </h1> '


# con rederización de otro archivo html
@app.route('/mostrar/<nombre>', methods=['GET', 'POST'])
def mostrar_nombre(nombre):
    return render_template('mostrar.html', nombre_parametro=nombre)

# redireccionar hacia otras paginas


@app.route('/redirect')
def mi_redirect():
    return redirect(url_for('hola_mundo'))

# error de pagina

# aqui ya no se usa route para la ruta, sino errorhandler


@app.errorhandler(404)
def pagina_error(error):
    return render_template('404.html', error=error), 404


# ruta evaluando usuario y contraseña

@app.route('/ingreso/<usuario>/<password>')
def evaluando(usuario, password):
    # simulando base de datos
    bd_usuario = "emerson"
    bd_password = "123456"

    # evaluando si cumple
    if bd_usuario == usuario and bd_password == password:
        return "Inicio exitoso"
    else:
        return "Datos incorrectos"

  # ruta para hacer una operación matemática


@app.route('/sumar/<dato1>/<dato2>')
def sumar(dato1, dato2):
    suma = int(dato1) + int(dato2)
    resultado = str(suma)
    return f'<h1> la suma de {dato1} mas la suma de {dato2} el resultado es: {resultado} </h1>'

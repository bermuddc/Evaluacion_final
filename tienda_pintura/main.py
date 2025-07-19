from flask import Flask, render_template, request

app = Flask(__name__)

USUARIOS = {
    "juan": {"password": "admin", "rol": "administrador"},
    "pepe": {"password": "user", "rol": "usuario"}
}


# página de inicio con botones
@app.route('/')
def index():
    return render_template('index.html')


# Cálculo de pintura
@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        tarros = int(request.form['tarros'])

        precio_tarro = 9000
        total_sin_descuento = tarros * precio_tarro

        if 18 <= edad <= 30:
            descuento = 0.15
        elif edad > 30:
            descuento = 0.25
        else:
            descuento = 0

        monto_descuento = total_sin_descuento * descuento
        total_con_descuento = total_sin_descuento - monto_descuento

        resultado = {
            'nombre': nombre,
            'total_sin_descuento': total_sin_descuento,
            'descuento': monto_descuento,
            'total_con_descuento': total_con_descuento
        }
        return render_template('ejercicio1.html', resultado=resultado)

    return render_template('ejercicio1.html')


# Sistema de login
@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    mensaje = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in USUARIOS and USUARIOS[username]['password'] == password:
            rol = USUARIOS[username]['rol']
            mensaje = f"Bienvenido {rol} {username}"
        else:
            mensaje = "Usuario o contraseña incorrectos"

    return render_template('ejercicio2.html', mensaje=mensaje)


if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '¡Hola, mundo! Esta es mi primera aplicación Flask.'

@app.route('/sitio1')
def sitio1():
    return 'Este es el sitio 1'

if __name__ == '__main__':
    app.run(debug=True)

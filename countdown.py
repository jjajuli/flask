from flask import Flask, render_template
from threading import Thread
import time

# Crear una aplicación Flask
app = Flask(__name__)

# Ruta para la página principal
@app.route('/')
def countdown():
    return render_template('countdown.html')

# Función para la cuenta regresiva
def countdown_thread():
    countdown = 100
    while countdown >= 0:
        time.sleep(1)
        countdown -= 1
        app.jinja_env.globals['countdown'] = countdown

# Función principal
if __name__ == '__main__':
    # Iniciar la cuenta regresiva en un hilo aparte
    countdown_thread = Thread(target=countdown_thread)
    countdown_thread.start()
    # Iniciar la aplicación Flask
    app.run(debug=True)

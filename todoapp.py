#import libreria Flask
from flask import Flask, render_template

app = Flask(__name__)

#ruta principal
@app.route('/')

def principal():
    return render_template('index.html')

#ruta contacto
@app.route('/contacto')

#Mensaje ruta de contacto
def contacto():
    return render_template('contacto.html')

#ruta de Lenuajes
@app.route('/lenguajes')

#Mensaje ruta de lenguajes
def lenguajes():
    return render_template('lenguajes.html')

#Main del programa
if __name__ == '__main__':
    #debug = True, para reiniciar automaticamente el servidor
    app.run(debug=True)
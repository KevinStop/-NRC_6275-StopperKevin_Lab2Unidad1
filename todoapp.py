#import libreria Flask
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

headings = ("Tarea","Correo Electronico", "Dificultad", "Descripcion")
data=(
    ("Investigar","rahep95022@sceath.com","Media","Investigar Flask")
    ("Mantenimiento","prollokuwewi-4597@yopmail.com","Alta","Realizar mantenimiento al equipo")
    ("Encender","zeknudakni@vusra.com","Baja","Encender el ordenador")
)

@app.route('/')
def helloworld():
    return render_template("index.html")

@app.route('/enviar')
def enviar():
    return render_template('enviar.html', headings=headings, data=data)

if __name__ == "__main__":
    app.run(debug=True)

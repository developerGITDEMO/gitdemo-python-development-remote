from flask import Flask, render_template, request, flash
from datetime import date, datetime
import webbrowser

from flask.wrappers import Request

app = Flask(__name__)
app.secret_key = "manbearpig_MUDMAN888"

#Saludo Hola
@app.route("/")
def index():
	flash("¿Cuál es tu nombre?")
	return render_template("index.html")

@app.route("/greet", methods=['POST', 'GET'])
def greeter():
	flash("Hola " + str(request.form['name_input']) + " !")
	return render_template("index.html")

#Cálculo de edad
@app.route("/bd")
def age():
	flash("¿Cuál es tu fecha de nacimiento?")
	return render_template("ageindex.html")

@app.route("/age", methods=['POST', 'GET'])
def agecalc():
	today = date.today()
	bd = request.form['date_input']
	birthday = datetime.strptime(bd, '%Y-%m-%d')
	age = today.year - birthday.year
	age -= ((today.month, today.day) < (birthday.month, birthday.day))
	flash("Tu edad es: " + str(age) + " años")
	return render_template("ageindex.html")

#Suma de dos números
@app.route("/sum")
def sum():
	flash("Ingrese los números a sumar")
	return render_template("sumindex.html")

@app.route("/sumresult", methods=['POST', 'GET'])
def sumcalc():
	num1 = request.form['n1_input']
	num2 = request.form['n2_input']
	intnum1 = int(num1)
	intnum2 = int(num2)
	sum = intnum1 + intnum2
	flash("La suma de los dos números es: " + str(sum) + " .")
	return render_template("sumindex.html")

HOST = "localhost"
PORT = 4000
DEBUG = True

if __name__ == '__main__':
	app.run(HOST, PORT, DEBUG)

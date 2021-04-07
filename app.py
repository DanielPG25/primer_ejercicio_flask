from flask import Flask, render_template
app = Flask(__name__)	


@app.route('/',methods=["GET","POST"])
def inicio():
	return render_template("index.html")

@app.route("/potencia/<int:base>/<int:exponente>",methods=["GET","POST"])
def saluda(cadena="NADIE",edad=1):
	resultado = potencia**exponente
	return render_template("potencia.html",base=base,exponente=exponente,resultado=resultado)

@app.route("/articulos/<int:numero>")
def mostrar_ariculo(numero):
    return render_template("articulos.html",id=numero)

app.run(debug=True)
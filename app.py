from flask import Flask, render_template
app = Flask(__name__)	


@app.route('/',methods=["GET","POST"])
def inicio():
	return render_template("index.html")

@app.route('/potencia/',methods=["GET","POST"])
@app.route("/potencia/<int:base>/<exponente>",methods=["GET","POST"])
def potencia(base=1,exponente=2):
	resultado = base**int(exponente)
	return render_template("potencia.html",base=base,exponente=exponente,resultado=resultado)

@app.route('/cuentaletras/',methods=["GET","POST"])
@app.route("/cuenta/palabra/letra",methods=["GET","POST"])
def cuentaletras(palabra="hola",letra="a"):
	if len(letra) > 1:
		abort(404)
	veces=palabra.count(letra)
	return render_template("cuentaletras.html",palabra=palabra,letra=letra,veces=veces)

app.run(debug=True)
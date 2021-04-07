from flask import Flask, render_template
app = Flask(__name__)	


@app.route('/',methods=["GET","POST"])
def inicio():
	return render_template("index.html")

@app.route('/potencia/',methods=["GET","POST"])
@app.route("/potencia/<int:base>/<int:exponente>",methods=["GET","POST"])
def potencia(base=1,exponente=2):
	resultado = base**exponente
	return render_template("potencia.html",base=base,exponente=exponente,resultado=resultado)


app.run(debug=True)
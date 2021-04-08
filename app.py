from flask import Flask, render_template, abort
from lxml import etree
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
@app.route('/cuenta/<palabra>/<letra>',methods=["GET","POST"])
def cuentaletras(palabra="hola",letra="a"):
	if len(letra) > 1:
		abort(404)
	veces=palabra.count(letra)
	return render_template("cuentaletras.html",palabra=palabra,letra=letra,veces=veces)

@app.route('/libros/',methods=["GET","POST"])
@app.route('/libro/<int:codigo>',methods=["GET","POST"])
def buscarlibro(codigo=127):
	xml='/home/danieldp/Documentos/github/primer_ejercicio_flask/libros.xml'
	fichero=etree.parse(xml)
	lista=fichero.xpath("/biblioteca/libro")
	codigo2 = str(codigo)
	for a in lista:
		if codigo2 in a.xpath("./codigo/text()"):
			autor=a.xpath("./autor/text()")
			titulo=a.xpath("./titulo/text()")
	return render_template("libros.html",autor=autor[0],nombre=titulo[0])		


app.run(debug=True)
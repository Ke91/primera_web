from flask import Flask
import random
app = Flask(__name__)

@app.route("/")
def hola_mundo():
    return '<h1>Hola, Mundo!</h1>'

lista_datos = [
    "Me gusta el fútbol.",  
    "Me gusta comer.",  
    "Me gusta dormir.",  
    "El estudio es agotador.",  
    "Me gusta la música.",
    "Me gustan los perros y gatos."
    "Los pulpos tienen tres corazones.",
    "La Vía Láctea tiene más de 100 mil millones de estrellas.",
    "Los tiburones existen desde antes que los dinosaurios.",
    "El corazón de una ballena azul puede pesar lo mismo que un coche pequeño.",
    "Las abejas pueden reconocer rostros humanos.",
    "Los plátanos son radiactivos en pequeñas cantidades.",
    "Recuerda respirar🤓.",
]

@app.route("/datos")
def base_de_datos():
    dato_aleatorio = random.choice(lista_datos)
    return f'<h1>{dato_aleatorio}</h1>'

app.run(debug=True)

@app.route("/moneda")
def lanzar_moneda():
    resultado = random.choice(["Cara", "Sello"])
    return f'<h1>Resultado del lanzamiento: {resultado}</h1>'
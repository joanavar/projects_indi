from flask import Flask, render_template, request, session, redirect, url_for
import random

app = Flask(__name__)
app.secret_key = "clave_secreta_para_la_sesion"  # Necesaria para usar sesiones

opciones = ["Piedra", "Papel", "Tijeras"]

@app.route("/", methods=["GET", "POST"])
def index():
    # Inicializar variables de sesión si es la primera vez
    if "puntos_jugador" not in session:
        session["puntos_jugador"] = 0
        session["puntos_ia"] = 0

    resultado = ""
    ia = ""
    jugador = ""

    if request.method == "POST":
        jugador = request.form["jugada"]
        ia = random.choice(opciones)

        if jugador == ia:
            resultado = "Empate"
        elif (jugador == "Piedra" and ia == "Tijeras") or \
             (jugador == "Papel" and ia == "Piedra") or \
             (jugador == "Tijeras" and ia == "Papel"):
            resultado = "Ganaste"
            session["puntos_jugador"] += 1
        else:
            resultado = "Perdiste"
            session["puntos_ia"] += 1

        # Verificar si alguien llegó a 3 puntos
        if session["puntos_jugador"] >= 3:
            resultado += " — ¡Ganaste la partida! 🎉"
            session["puntos_jugador"] = 0
            session["puntos_ia"] = 0
        elif session["puntos_ia"] >= 3:
            resultado += " — La IA ganó la partida 😢"
            session["puntos_jugador"] = 0
            session["puntos_ia"] = 0

    return render_template("index.html",
                           jugador=jugador,
                           ia=ia,
                           resultado=resultado,
                           puntos_jugador=session["puntos_jugador"],
                           puntos_ia=session["puntos_ia"])

if __name__ == "__main__":
    app.run(debug=True, port=5001)

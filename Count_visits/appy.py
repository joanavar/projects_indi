from flask import Flask, request, session, render_template, redirect, url_for

app = Flask(__name__)
app.secret_key = "Clave_secreta_para_contador"
methods = ["GET", "POST"]

@app.route("/", methods=methods)
def index():
    if "visitas" not in session:
        session["visitas"] = 0
    
    if request.method == "POST":
        if request.form.get("accion") == "sumar":
            session["visitas"] += 1
        if request.form.get("accion") == "reiniciar":
            session["visitas"] = 0
        return redirect(url_for("index"))

    return render_template("index.html", visitas = session["visitas"])
if __name__ == "__main__":
    app.run(debug=True, port=5002)
from flask import Flask, request, session, render_template, redirect, url_for

app = Flask(__name__)
app.secret_key= "Clave_secreta_lista"

@app.route("/", methods=["GET", "POST"])
def index():
    if "tareas" not in session:
        session["tareas"] = []
    if request.method == "POST":
        accion = request.form.get("accion")
        if accion == "agregar":
            tarea_nueva = request.form.get("tarea")
            if tarea_nueva:
                session["tareas"].append(tarea_nueva)
                session.modified = True
        elif accion == "Borrar_todo":
            session["tareas"] = []
            session.modified = True
        return redirect(url_for("index"))
    return render_template("index.html", tareas=session["tareas"])
if __name__ == "__main__":
    app.run(debug=True, port=5001)
    
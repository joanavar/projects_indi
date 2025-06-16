from flask import Flask, redirect, request, render_template, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tareas.db" # Archivo DB local
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class Tarea(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(200), nullable = False)

with app.app_context():
    db.create_all()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        accion = request.form.get("accion")
        if accion == "agregar":
            tarea_nueva = request.form.get("tarea")
            if tarea_nueva:
                nueva_tarea = Tarea(descripcion= tarea_nueva)
                db.session.add(nueva_tarea)
                db.session.commit()
        elif accion == "Borrar_todo":
            Tarea.query.delete()
            db.session.commit()
        return redirect(url_for("index"))
    tareas = Tarea.query.all()
    return render_template("index.html", tareas=tareas)
if __name__ == "__main__":
    app.run(debug=True, port=5002)
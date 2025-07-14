from flask import Flask, render_template
 
app = Flask(__name__)

menu = {
    "Inicio": {},
    "Oferta Educativa": {
        "Licenciaturas e Ingenierías": {
            "Licenciatura en Administración": {
                "Plan de Estudios": {},
                "Programa": {},
                "Descripción": "Forma profesionales capaces de administrar eficientemente los recursos de las organizaciones, desarrollando habilidades en gestión empresarial, finanzas, marketing y recursos humanos."
            },
            "Ingeniería en Sistemas Computacionales": {
                "Plan de Estudios": {},
                "Programa": {}
            },
            "Ingeniería Electrónica": {
                "Plan de Estudios": {},
                "Programa": {}
            }
        },
        "Maestrías": {
            "Maestría en Ciencias de la Computación": {
                "Plan de Estudios": {},
                "Programa": {}
            },
            "Maestría en Administración": {
                "Plan de Estudios": {},
                "Programa": {}
            }
        },
        "Posgrados": {
            "Doctorado en Innovación Educativa": {
                "Plan de Estudios": {},
                "Programa": {}
            },
            "Doctorado en Ciencias Computacionales": {
                "Plan de Estudios": {},
                "Programa": {}
            }
        }
    },
    "Contacto": {}
}

@app.route("/")
def index():
    return render_template("menu.html", menu=menu)
 
if __name__ == "__main__":
    app.run(debug=True)

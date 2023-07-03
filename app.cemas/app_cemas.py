from flask import Flask, render_template

app = Flask(__name__)


#-----------------------Login-------------------------------------------------------

@app.route("/login")
def login():
    return render_template("login.html")

#------------------------------------------------------------------------------

#--------------------------Libro----------------------------------------------------


@app.route("/libro")
def libro():
    return render_template ("reg_btn_libro.html")
    
@app.route("/reg_libro")
def reg_libro():
    return render_template("reg_libro.html")


#-------------------------------fin de libro--------------------------------------------------


#-----------------------Pag. pricipal-------------------------------------------------


@app.route("/index")
def index():
    return render_template("index.html") 

#-----------------------Fin pag. pricipal----------------------------------------------------------





#-----------------------Admin Personal-------------------------------------------------

@app.route("/reg_personal_admin")
def reg_personal_admin():
    return render_template("reg_personal_admin.html")


#----------------------Fin estudiante-------------------------------------------------




#-----------------------Estudiante-------------------------------------------


@app.route("/estudiante")
def estudiante():
    return render_template("reg_estudiante.html")


#-------------------------Fin estudiante---------------------------------------------------

@app.route("/asignaturas")
def asignaturas():
    return render_template ("reg_asignaturas.html")
    
@app.route("/asignaturasbtn")
def asignaturasbtn():
    return render_template("reg_btn_asignaturas.html")






if __name__ == '__main__':
    app.run(debug=True)
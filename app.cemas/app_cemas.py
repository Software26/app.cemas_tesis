from flask import Flask, render_template

app = Flask(__name__)


#-----------------------Login-------------------------------------------------------

@app.route("/login")
def login():
    return render_template("login.html")

#------------------------------------------------------------------------------

#--------------------------Libro----------------------------------------------------


@app.route("/librobtn")
def librobtn():
    return render_template("librobtn.html")
    
@app.route("/libro")
def libro():
    return render_template("libro.html")


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
    return render_template("asignaturas.html")
    
@app.route("/asignaturasbtn")
def asignaturasbtn():
    return render_template("asignaturasbtn.html")

#----------------------------------------------------------------------------------------------------
@app.route("/boetin")
def boletin():
    return render_template("")
    
@app.route("/boletinbtn")
def boletinbtn():
    return render_template("boletinbtn.html")
#--------------------------------------------------------------------------------------------------
"""
@app.route("/")
def boletin():
    return render_template("")
    
@app.route("/boletinbtn")
def boletinbtn():
    return render_template("boletinbtn.html")

"""


if __name__ == '__main__':
    app.run(debug=True)
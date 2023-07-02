from flask import Flask, render_template

app = Flask(__name__)

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/index")
def pagina2():
    return render_template("index.html") #este es el enlce a la herecia 1.html


@app.route("/reg_personal_admin")
def prueba():
    return render_template("reg_personal_Admin.html")



@app.route("/estudiante")
def estudiante():
    return render_template("reg_estudiante.html")






if __name__ == '__main__':
    app.run(debug=True)
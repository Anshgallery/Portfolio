from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("exhibition.html")


@app.route("/details")
def details():
    return render_template("welcome.html")


@app.route("/certification")
def certification():
    return render_template("certification.html")


@app.route("/projects")
def projects():
    return render_template("project.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/resume")
def resume():
    return render_template("resume.html")

@app.route("/experence")
def experence():
    return render_template("experence.html")

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0" ,port=8080)
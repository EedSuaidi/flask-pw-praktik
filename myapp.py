from flask import Flask

app = Flask(__name__)

@app.route("/")

def index():
    return "<h1 style='color: red; font-family: arial; text-align: center; font-size: 200px;'>Halo, Dunia</h1>"

if __name__ == "__main__":
    app.run(debug=True)

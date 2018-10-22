from gpiozero import LED
from flask import Flask

app = Flask(__name__)
led = LED(17)

@app.route("/")

def ready():
    return "Server beschikbaar\n"

@app.route("/knopin")

def knopin():
    return "Knop gedrukt!\n"

@app.route("/knopuit")

def knopuit():
    return "Knop losgelaten!\n"

if __name__ == '__main__':
    app.run(host='0.0.0.0')
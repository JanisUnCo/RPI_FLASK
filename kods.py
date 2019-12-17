from flask import Flask, render_template
import RPi.GPIO as GPIO

app = Flask(__name__)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(19,GPIO.OUT)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cakes')
def cakes():
    return render_template('cakes.html')

@app.route('/?fname=<vards>')
def gaisma(vards):
    if vards == "janis":
        GPIO.output(13,GPIO.HIGH)
        GPIO.output(19,GPIO.HIGH)

    return render_template('gaisma.html')


@app.route('/hello/<name>')
def hello(name):
    return render_template('page.html', name=name)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
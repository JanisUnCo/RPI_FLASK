from flask import Flask, render_template
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(13,GPIO.OUT)


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
    GPIO.output(13,GPIO.LOW)

@app.route('/cakes')
def cakes():
    return render_template('cakes.html')
    GPIO.output(13,GPIO.HIGH)
    

@app.route('/hello/<name>')
def hello(name):
    return render_template('page.html', name=name)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
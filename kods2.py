from flask import Flask, redirect, url_for, render_template
import RPi.GPIO as GPIO

app = Flask(__name__)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(19,GPIO.OUT)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/cakes')
def cakes():
    return render_template('cakes.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
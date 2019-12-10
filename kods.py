from flask import Flask, render_template
import RPi.GPIO as GPIO

app = Flask(__name__)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(13,GPIO.OUT)

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

@app.route("/readPin/<pin>")
def readPin(pin):
   try:
      GPIO.setup(int(pin), GPIO.IN)
      if GPIO.input(int(pin)) == True:
         response = "Pin number " + pin + " is high!"
      else:
         response = "Pin number " + pin + " is low!"
   except:
      response = "There was an error reading pin " + pin + "."

   templateData = {
      'title' : 'Status of Pin' + pin,
      'response' : response
      }

   return render_template('pin.html', **templateData)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
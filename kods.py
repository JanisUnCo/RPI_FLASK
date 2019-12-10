from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Kaka ir ok'

if __name__ == '__main__':
    app.run(debug=True, host='192.168.43.107')
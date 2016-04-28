from flask import Flask
app = Flask(__name__)

@app.route('/')
def HelloWorld():
    return 'Hello World'

@app.route('/user'):
def UserTest():
    return 'User Base Page'

@app.route('/user/<uncastname>')
def UncastTest(uncastname):
    return uncastname

@app.route('/user/<int:castname>')
def CastTest(castname):
    return castname * 10

if __name__ == '__main__':
    app.debug = True
    app.run('0.0.0.0')

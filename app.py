from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "<h1>Hello World :)</h1>"


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return "Hello {}".format(name)


@app.route('/f')
@app.route('/f/<celsius>')
def celsius_to_fahrenheit(celsius=""):
    """ """
    result = float(celsius) * 9.0 / 5 + 32
    return "<h1>{}</h1>".format(result)


if __name__ == '__main__':
    app.run()

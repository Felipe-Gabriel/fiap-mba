from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "<h1>Hola FIAP! versão 2</h1>\nMBA! o/"

if __name__ == '__main__':
    application.run()

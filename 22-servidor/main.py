from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Hola, Lentamos el primer server.'

if __name__ == '__main__':
  app.run()
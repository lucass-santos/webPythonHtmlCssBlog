from flask import Flask

app = Flask("hello")

@app.route("/")
def hello():
    return "Hello World!"


@app.route("/contatos")
def contato():
    return """<html>
                <head>
                    <title> Contatos </title>
                </head>
                <body>
                    <h1>Lucas Santos de Oliveira</h1>
                    <h2>Rua tra la la</h2>
                    <h3>Telefone: (11)98525-6341</h3>
                </body>
              </html>"""
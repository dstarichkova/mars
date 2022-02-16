from flask import Flask, url_for

app = Flask(__name__)


@app.route("/")
def main():
    return "Миссия Колонизация Марса"


@app.route("/index")
def index():
    return "И на Марсе будут яблони цвести!"


@app.route("/promotion")
def promotion():
    text = ['Человечество вырастает из детства.', 'Человечеству мала одна планета.',
            'Мы сделаем обитаемыми безжизненные пока планеты.', 'И начнем с Марса!',
            'Присоединяйся!']
    return "</br>".join(text)


@app.route("/image_mars")
def image_mars():
    return f"""<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <title>Привет, Марс!</title>
                      </head>
                      <body>
                        <h1>Жди нас, Марс!</h1>
                        <img src="{url_for('static', filename='img/mars.jpg')}" 
                        alt="здесь должна была быть картинка, но не нашлась">
                        </br>Вот она какая, красная планета.
                      </body>
                    </html>"""


@app.route("/promotion_image")
def promotion_image():
    # with open('design.html', 'r', encoding='utf-8') as html_stream:
    #     return html_stream.read()
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
    <title>Колонизация</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
</head>
<body>
<h1>Жди нас, Марс!</h1>
<img src="{url_for('static', filename='img/mars.jpg')}" 
                        alt="здесь должна была быть картинка, но не нашлась">
<div class="alert alert-dark" role="alert">
  Человечество вырастает из детства.
</div>
<div class="alert alert-success" role="alert">
  Человечеству мала одна планета.
</div>
<div class="alert alert-secondary" role="alert">
  Мы сделаем обитаемыми безжизненные пока планеты.
</div>
<div class="alert alert-warning" role="alert">
  И начнем с Марса!
</div>
<div class="alert alert-danger" role="alert">
  Присоединяйся!
</div>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
</body>
</html>"""


if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")

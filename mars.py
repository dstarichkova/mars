from flask import Flask, url_for, request

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


# @app.route('/astronaut_selection', methods=['POST', 'GET'])
# def astronaut_selection():
#     if request.method == 'GET':
#         return f'''<!doctype html>
#                         <html lang="en">
#                           <head>
#                             <meta charset="utf-8">
#                             <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
#                             <link rel="stylesheet"
#                             href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
#                             integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
#                             crossorigin="anonymous">
#                             <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
#                             <title>Пример формы</title>
#                           </head>
#                           <body>
#                             <h1>Форма для регистрации в суперсекретной системе</h1>
#                             <div>
#                                 <form class="login_form" method="post">
#                                     <input type="text" class="form-control" id="lastname" aria-describedby="lastnameHelp" placeholder="Введите фамилию" name="lastname">
#                                     <input type="text" class="form-control" id="name" aria-describedby="nameHelp" placeholder="Введите имя" name="name">
#                                     <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
#                                     <input type="password" class="form-control" id="password" placeholder="Введите пароль" name="password">
#                                     <div class="form-group">
#                                         <label for="classSelect">Какое у Вас образование?</label>
#                                         <select class="form-control" id="classSelect" name="class">
#                                           <option>Начальное</option>
#                                           <option>Среднее</option>
#                                           <option>Высшее</option>
#                                         </select>
#                                      </div>
#                                     </div>
#                                     <div class="form-group">
#                                         <label for="form-check">Какие у Вас есть профессии?</label>
#                                         <div class="form-check">
#                                           <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
#                                           <label class="form-check-label" for="male">
#                                             Мужской
#                                           </label>
#                                         </div>
#                                         <div class="form-check">
#                                           <input class="form-check-input" type="radio" name="sex" id="female" value="female">
#                                           <label class="form-check-label" for="female">
#                                             Женский
#                                           </label>
#                                         </div>
#                                     </div>
#                                     <div class="form-group">
#                                         <label for="about">Немного о себе</label>
#                                         <textarea class="form-control" id="about" rows="3" name="about"></textarea>
#                                     </div>
#                                     <div class="form-group">
#                                         <label for="photo">Приложите фотографию</label>
#                                         <input type="file" class="form-control-file" id="photo" name="file">
#                                     </div>
#                                     <div class="form-group">
#                                         <label for="form-check">Укажите пол</label>
#                                         <div class="form-check">
#                                           <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
#                                           <label class="form-check-label" for="male">
#                                             Мужской
#                                           </label>
#                                         </div>
#                                         <div class="form-check">
#                                           <input class="form-check-input" type="radio" name="sex" id="female" value="female">
#                                           <label class="form-check-label" for="female">
#                                             Женский
#                                           </label>
#                                         </div>
#                                     </div>
#                                     <div class="form-group form-check">
#                                         <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
#                                         <label class="form-check-label" for="acceptRules">Готов быть добровольцем</label>
#                                     </div>
#                                     <button type="submit" class="btn btn-primary">Записаться</button>
#                                 </form>
#                             </div>
#                           </body>
#                         </html>'''
#     elif request.method == 'POST':
#         print(request.form['email'])
#         print(request.form['password'])
#         print(request.form['class'])
#         print(request.form['file'])
#         print(request.form['about'])
#         print(request.form['accept'])
#         print(request.form['sex'])
#         return "Форма отправлена"


@app.route("/results/<nickname>/<int:level>/<float:rating>")
def results(nickname, level, rating):
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <title>Привет, Яндекс!</title>
                  </head>
                  <body>
                    <h1>Результаты отбора</h1>
                    <h3>Претендента на участие в миссии {nickname}:</h3>
                    <div class="alert alert-success" role="alert">
                      Поздравляем! Ваш рейтинг после {level} этапа отбора
                    </div>
                    <div class="alert alert-light" role="alert">
                      Составляет {rating}!
                    </div>
                    <div class="alert alert-warning" role="alert">
                      Желаем удачи!
                    </div>
                  </body>
                </html>'''


if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")

from flask import Flask
from random import randint

app = Flask(__name__)
random_number = randint(0, 9)

@app.route('/')
def hello():
    return '<h1 style="color:#03C04A">Guess a number between 0 and 9</h1>' \
           '<p><em>Type number in route: e.g. /7</em>' \
           '<br />' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" alt="numbers" />'

@app.route('/<int:user_number>')
def greet(user_number):
    if user_number < random_number:
        return '<h1 style="color:red">Too Low. try again</h1>'\
               '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif" />'
    elif user_number > random_number:
        return '<h1 style="color:red">Too High. try again</h1>'\
                '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif" />'
    else:
        return '<h1 style="color:#3944BC">Nice!</h1>'\
               '<img src="https://media0.giphy.com/media/yJFeycRK2DB4c/giphy.gif?cid=ecf05e478bkljbme5ekl5dem7jlgcph2chlf21yietbegxth&rid=giphy.gif&ct=g" />'

if __name__ == '__main__':
    app.run(debug=True)
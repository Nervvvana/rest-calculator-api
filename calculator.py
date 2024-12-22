from flask import Flask
import re
import math
app = Flask(__name__)


@app.route('/')
def index():
    return '<h1 align="center">Введите пример в адресную строку</h1>'


@app.route('/<example>')
def calculate(example):
    e = re.match('-?[0-9]+[+-:*]-?[0-9]+', example)
    c = re.match('cylinder[(]r=[0-9]+,h=[0-9]+[)]', example)
    if e and len(e.group()) == len(example):
        return '<h1 align="center">%s</h1>' % calculator(e)
    if c and len(c.group()) == len(example):
        return '<h2 align="center">%s</h2>' % cylinder_info(c)
    return '<h1 align="center">Некорректный ввод!</h1>'



def cylinder_info(c):
    ex = c.group()
    pi = math.pi
    radius = float(ex[11:ex.find(',')])
    height = float(ex[ex.find('h') + 2: len(ex) - 1])
    base_area = pi * radius * radius
    side_area = 2 * pi * radius * height
    full_area = 2 * base_area + side_area
    volume = base_area * height
    return ('Площадь основания цилиндра: %s<br>'
           ' Площадь боковой поверхности цилиндра: %s<br>'
           ' Общая площадь цилиндра: %s<br>'
           ' Объём цилиндра: %s') % (base_area, side_area, full_area, volume)


def calculator(e):
    ex = e.group()
    num1 = re.match('-?[0-9]+', ex).group()
    ex = ex[len(num1):]
    num1 = int(num1)
    sign = ex[0]
    ex = ex[1:]
    num2 = int(ex)
    match sign:
        case '+':
            res = num1 + num2
        case '-':
            res = num1 - num2
        case ':':
            if num2 == 0:
                return '<h1 align="center">Деление на ноль невозможно</h1>'
            res = num1 / num2
        case '*':
            res = num1 * num2
    return '%s %s %s = %s' % (num1, sign, num2, res)


if __name__ == '__main__':
    app.run()
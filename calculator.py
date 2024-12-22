from flask import Flask
import re
import math
app = Flask(__name__)


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
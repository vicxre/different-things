#ввод диапозона рандома
import random as r


try:
    ot = int(input('от скольки будет рандом ->'))
    do = int(input('до скольки будет рандом ->'))

    result = r.randint(ot,do)

    print('результат рандома -> ', result)

except ValueError:
    print("nefiga!!!")
    print('введи цифарки')

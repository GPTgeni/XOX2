def main():

    # 1 заданеи
    a = input("напиши слово")
    if a == "Python":
        print('ДА')
    else:
        print('НЕТ')


    # 2 задание
    f = input()
    g = input()
    if ('да' or 'нет') in (f and g):
        print('ВЕРНО')
    else:
        print('НЕВЕРНО')

    # 3 задание
    q = input()
    w = input()
    e = input()
    if ("1" and "2" and "3") in (q and w and e):
        print('ГОРИ')
    elif ('раз' and 'два' and 'три') in (q and w and e):
        print('ГОРИ')
    else:
        print('НЕГОРИ')

    # 4 задание
    j = input()
    a = input()
    if j == 'Тула' and a == 'Пенза':
        print('НЕТ')
    else:
        print('ДА')

    # 5 задание
    g = int(input("дистанция марафона: "))
    f = int(input("спортсмен пробегает за день: "))
    import math
    s = math.ceil(g / f)
    print("Спортсмен достигнет финиша на", s, "день.")

    # 8 задание
    c = int(input())
    a = int(input())
    t = int(input())
    y = c + a + t
    if c < a < t:
        print('Акция!')
        print('К оплате:', y // 2)
    elif c > a > t:
        print('Акция!')
        print('К оплате:', y // 3)
    else:
        print('К оплате:', y)

    # 9 задание
    g = int(input('За вчера: '))
    h = int(input('За позавчера: '))
    if g < h:
        print('Сегодня магазин посетит:', g + (g - h), 'человек')
    elif g > h:
        print('Сегодня магазин посетит:', g - (g - h), 'человек')
    else:
        print('Сегодня магазин посетит:', g, 'человек')

    # 10 задание
    c = int(input())
    if (c % 4 == 0) and (c % 100 != 0) or (c % 400 == 0):
        print('Является високоcным годом')
    else:
        print('Не является високосным годом')

    # 11 задание
    s = int(input())
    if s % 2 == 0:
        print('Четное число')
    else:
        print('Нечентное число')


if __name__ == "__main__":
    main()
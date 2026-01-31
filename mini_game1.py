import random
import time
print("Компьютер загадывает число от 1 до 10.")
time.sleep(1)
print("...")
time.sleep(1.5)
print("У Игрока 3 попытки угадать.")
time.sleep(2)
print("Победа - выход. Неудача - подсказка:")
time.sleep(0.2)
print("*больше")
time.sleep(0.5)
print("*меньше")
time.sleep(3)
print("Давай начинать.")
ready = input("Ты готов? Да/Нет: ").lower()

if ready != "да":
    print("Конец.")
else:
    print("Начинаем...")

    secret = random.randint(1,10)
    attempts = 3

    while attempts > 0:
        guess = int(input("Угадывай: "))
        if guess == secret:
            print("Ты победил!")
            break
        elif guess < secret:
            print("*больше")
        else:
            print("*меньше")
        attempts -= 1

    if attempts == 0:
        print("Ты проиграл. Число было:", secret)





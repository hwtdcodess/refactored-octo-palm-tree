num = int(input("число от 1 до 5: "))
for i in range(1, num + 1):
    print(i)
# от 1 до выбранного числа

num2 = int(input("число, которое нужно умножить: "))
num3 = int(input("число, на которое умножать: "))
print (num2 * num3)
# простой калькулятор с умножением
num4 = int(input("число: "))
if num4 % 2 == 0:
    print (num4 * 2)
else:
    print (num4 * 3)
# если четное * 2, нечетное * 3
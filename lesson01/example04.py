# 4. Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.


число = abs(int(input("Введите целое положительное число >>>")))
max = число % 10
while число >= 1:
    число = число // 10
    if число % 10 > max:
        max = число % 10
    if число > 9:
        continue
    else:
        print("Максимальное цифра в числе", max)
        break
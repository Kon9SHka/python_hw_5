# Задача 26: Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

def get_result (a,b):
    if b == 0:
        return 1
    return a * get_result(a,b-1)

a = int(input("Введите число, которое вводим в степень: "))
b = int(input("Введите степень: "))

print(get_result(a,b))
from my_module import summa
import math

def ln(x):
    if x <= 0:
        return "Число должно быть больше нуля"
    return math.log(x)

def log10(x):
    if x <= 0:
        return "ошибка: число должно быть > 0"
    return math.log10(x)

def log_osn(x, a):
    if x <= 0 or a <= 0 or a == 1:
        return "Ошибка: числа должны быть больше нуля, а основание = 1"
    return math.log(x, a)

def summ(a, b):
    return a + b

def sq(n):
    if n < 0:
        return "Ошибка, число отрицательное"
    return math.sqrt(n)

def stepen(a, b):
    return a ** b
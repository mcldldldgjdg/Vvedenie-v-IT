import math
print("For Emperor, for our duty")
name=(str(input("Enter your name: ")))
def greet(name):
   print("Привет, " + name + "!")
greet(name)
number=int(input("Придуммай число чтобы возвести его в квадрат: "))
def square(number):
    print(number ** 2)
square(number)
x,y=(int(input("Придумай число x, что бы сравнить его с y: ")),
     int(input("Придумай число y, что бы сравнить его с x: ")))
def max_of_two(x,y):
    if x>y:
        return x
    elif x==y:
        return "equal"
    else:
        return y
print(max_of_two(x,y))
age=int(input("Enter your age: "))
def describe_person(name,age):
    greet(name)
    print("Ему:",age)
describe_person(name,age)
number=float(input("Придумай простое число "))
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True
print(is_prime(number))
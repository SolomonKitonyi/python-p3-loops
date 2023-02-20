#!/usr/bin/env python3

def happy_new_year():
    # code goes here
    num = 10
    while  num > 0:
        print(num)
        num -= 1
    print("Happy New Year!")

def square_integers(int_list):
    # code goes here
    return [num * num for num in int_list]

def fizzbuzz():
    # code goes here
    for num in range(1,101):
        if not num % 15:
            print("FizzBuzz")
        elif not num % 5:
            print("Buzz")

        elif not num % 3:
            print("Fizz")
        else:
            print(num)

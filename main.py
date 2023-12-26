import sys
def mult (a, b) :
    return a*b


def add (a, b) :
    return a+b


def sub (a, b) :
    return a/b


def min (a, b) :
    return a-b

def calculate (a,b) :
    if operation =="*" :
        return mult (a, b)
    elif operation == "+" :
        return add (a, b)
    elif operation == "/" :
        return sub (a, b)
    else:
        return min (a, b)


first = int(input("what's the first number?:   "))
operation = input("+\n-\n*\n/\nPick an operation: ")
second = int(input("what's the next number?:   "))


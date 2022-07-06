

def greet(name):
    print("Hello " + name)

def name_input():
    print("What is your name?")
    name = input()
    return name

greet(name_input())

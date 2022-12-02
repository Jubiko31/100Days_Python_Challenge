# Welcome to basic algebra calculator
from replit import clear
from art import logo

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

def calculator():
    print(logo)
    valid_operations = []

    num1 = float(input('Enter first number: '))
    for symbol in operations:
        valid_operations.append(symbol)
        print(symbol)
        
    is_over = False 
    while not is_over:
        operation = input('Which operation would you like to execute? ')
        if operation not in valid_operations:
            return "Enter valid operation. This is not NASA's calculator!"   
        num2 = float(input('Enter second number: '))
        calculate = operations[operation]
        res = calculate(num1, num2)
        
        print(f"{num1} {operation} {num2} = {res}")
    
        if input(f"Type 'y' to continue calculating with {res}, or type 'n' to start a new calculation: ") == 'y':
          num1 = res
        else:
            is_over = False
            clear()
            calculator()
            
calculator()
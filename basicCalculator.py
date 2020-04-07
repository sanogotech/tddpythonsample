"""
Python is an object oriented programming language: POO
Almost everything in Python is an object, with its properties and methods.
A Class is like an object constructor, or a "blueprint" for creating objects.
To create a class, use the keyword class:
"""
class Calculator:
    
    def addition(self,a,b):
        resultcalcul = a +b
        return resultcalcul

    def subtraction(self,a,b):
        resultcalcul = a - b
        return resultcalcul

    def multiplication(self,a,b):
        resultcalcul = a * b
        return resultcalcul

    def division(self,a,b):
        resultcalcul = (a / b)
        return resultcalcul

    
"""
In Python, function is a group of related statements that perform a specific task.
Functions help break our program into smaller and modular chunks.
Keyword def marks the start of function header.
A function name to uniquely identify it.
Parameters (arguments) through which we pass values to a function. They are optional.
An optional return statement to return a value from the function.
"""
def saisirClavier(message):
        saisie = input(message)
        return saisie
        
# Display result
def afficherResultat(operation,resultat):
        print("le resultat de ",operation ,"est : ", resultat)           

def startCalculatorMenu():
    # Init parameters
    # A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.
    menuoperationtuple = ("ADDITION", "SUBTRACTION", "MULTIPLICATION", "DIVISION")
    a = int(input("Enter first number:"))
    b = int(input("Enter second number:"))
    calculator = Calculator()
    choice = 1
    
   
    #Python has two primitive loop commands : While and For
    #While
    while choice != 0:
        print("---------------------------")
        print("1. ADDITION")
        print("2. SUBTRACTION")
        print("3. MULTIPLICATION")
        print("4. DIVISION")
        print("0. QUITTER LE MENU !")
        print("---------------------------")
        
        #Choice
        choice = int(input("Enter your choice:"))
        
        #Test If
        if choice == 1:
            resultat = calculator.addition(a,b)
            afficherResultat(menuoperationtuple[0],resultat)
        elif choice == 2:
            resultat = calculator.subtraction(a,b)
            afficherResultat(menuoperationtuple[1],resultat)
        elif choice == 3:
            resultat = calculator.multiplication(a,b)
            afficherResultat(menuoperationtuple[2],resultat)
        elif choice == 4:
            resultat = calculator.division(a,b)
            afficherResultat(menuoperationtuple[3],resultat)
        elif choice == 0:
            print(" Quitter le Menu !")
        else:
            print("Invalid choice")

# main function
def main():
    startCalculatorMenu()
    

if __name__ == '__main__':
    main()
    
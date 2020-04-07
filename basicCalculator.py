# Class Calculator
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

    
# Input
def saisirClavier(message):
        saisie = input(message)
        return saisie
        
# Display result
def afficherResultat(operation,resultat):
        print("le resultat de ",operation ,"est : ", resultat)           

def startCalculatorMenu():
    # Init parameters
    a = int(input("Enter first number:"))
    b = int(input("Enter second number:"))
    calculator = Calculator()
    choice = 1
    
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
            afficherResultat("ADDITION",resultat)
        elif choice == 2:
            resultat = calculator.subtraction(a,b)
            afficherResultat("SUBTRACTION",resultat)
        elif choice == 3:
            resultat = calculator.multiplication(a,b)
            afficherResultat("MULTIPLICATION",resultat)
        elif choice == 4:
            resultat = calculator.division(a,b)
            afficherResultat("DIVISION",resultat)
        elif choice == 0:
            print(" Quitter le Menu !")
        else:
            print("Invalid choice")

# main function
def main():
    startCalculatorMenu()
    

if __name__ == '__main__':
    main()
    
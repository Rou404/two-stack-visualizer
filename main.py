from calculator import calculator
from visualizer import visualizer

def driver():
    print("Please insert the number of the desired language: \n [1]Logical Connectives \n [2]Mathematical expression \n [3]Quit")
    x = int(input())
    if x == 1:
        print("Logical output")
    elif x == 2:
        print("Would you like to convert from or to polish notation? \n [1]Visualize expression \n [2]Compute expression")
        y = int(input())
        if y == 1:
            print("Please insert the expression with spaces between characters. Example: ( A + B ) * C / ( D - E )")
            visualizer(input())
        elif y == 2:
            print("Please insert the expression with spaces between characters. Example: ( 1 + 2 ) * 3 / ( 4 - 5 )")
            calculator(input())
    print("Would you like to try something else[Y/N]")
    if (str(input()) in "Yy"):
        driver()
driver()
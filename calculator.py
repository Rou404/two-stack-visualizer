# This is an optional project for Formal Languages and Automata Theory 2021-2022.
# Done by Stegeran Darius Cosmin 1
from tabulate import tabulate

stack = []

def readfrominput(exp):
    expression = [x for x in exp.split(" ")]
    operator = []
    operator_value = {"+": 1, "-": 1, "*": 2, "/": 2, "(": 0, ")": 0, "^": 3, "%": 2}
    final = []
    for token in expression:
        if token.isdigit():
            stack.append(int(token))
        elif token == "(":
            operator.append(token)
        elif token == ")":
            while operator and operator[-1] != "(":
                calculator(operator[-1])
                operator.pop()
                final.append([token, " ".join(operator), " ".join([str(x) for x in stack])])
            operator.pop()
        elif token in operator_value.keys():
            while len(operator) and operator_value[operator[-1]] >= operator_value[token]:
                calculator(operator[-1])
                operator.pop()
                final.append([token, " ".join(operator), " ".join([str(x) for x in stack])])
            operator.append(token)
        else:
            stack.append(int(token))
        final.append([token," ".join(operator)," ".join([str(x) for x in stack])])
    while len(operator):
        calculator(operator[-1])
        operator.pop()

        if operator:
            final.append([operator[-1]," ".join(operator)," ".join([str(x) for x in stack])])
        else:
            final.append([" ","Result is: ", stack.pop()])

    print(tabulate(final, headers = ["Token", "Operator Stack", "Evaluation Stack"], tablefmt="grid"))

def calculator(exp):
    match exp:
        case "+":
            aux = stack.pop() + stack.pop()
            stack.append(aux)
        case "-":
            a = stack.pop()
            aux = stack.pop() - a
            stack.append(aux)
        case "*":
            aux = stack.pop() * stack.pop()
            stack.append(aux)
        case "/":
            a = stack.pop()
            aux = stack.pop() / a
            stack.append(float("{:.2f}".format(aux)))
        case "%":
            a = stack.pop()
            aux = stack.pop() % a
            stack.append(float("{:.2f}".format(aux)))
        case "^":
            a = stack.pop()
            b = stack.pop()
            if b < 0:
                aux = -b ** a
            else:
                aux = b ** a
            stack.append(float("{:.2f}".format(aux)))

readfrominput("110 + ( 20 - ( 30 * ( 40 / ( 50 + ( 60 ^ 2 ) ) ) ) )")
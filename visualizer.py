# This is an optional project for Formal Languages and Automata Theory 2021-2022.
# Done by Stegeran Darius Cosmin1
from tabulate import tabulate

stack = []

def visualizer(exp):
    expression = [x for x in exp.split(" ")]
    operator = []
    operator_value = {"+": 1, "-": 1, "*": 2, "/": 2, "(": 0, ")": 0, "^": 3, "%": 2}
    final = []
    for token in expression:
        if token.isalnum():
            stack.append(str(token))
        elif token == "(":
            operator.append(token)
        elif token == ")":
            while operator and operator[-1] != "(":
                calculator(operator[-1])
                operator.pop()
            aux = "("+stack.pop()+")"
            stack.append(aux)
            operator.pop()
        elif token in operator_value.keys():
            while len(operator) and operator_value[operator[-1]] >= operator_value[token]:
                calculator(operator[-1])
                operator.pop()
            operator.append(token)
        else:
            stack.append(str(token))
        final.append([token, " ".join(operator), " ".join([str(x) for x in stack])])
    while len(operator):
        calculator(operator[-1])
        operator.pop()
        if operator:
            final.append([" ", " ".join(operator), " ".join([str(x) for x in stack])])
        else:
            final.append([" ", "Result is: ", stack.pop()])

    print(tabulate(final, headers = ["Token", "Operator Stack", "Evaluation Stack"], tablefmt="grid"))

def calculator(exp):
    match exp:
        case "+":
            a = stack.pop()
            aux = stack.pop() + " + " + a
            stack.append(aux)
        case "-":
            a = stack.pop()
            aux = stack.pop() + " - " + a
            stack.append(aux)
        case "*":
            a = stack.pop()
            aux = stack.pop() + " * " + a
            stack.append(aux)
        case "/":
            a = stack.pop()
            aux = stack.pop()+" / "+a
            stack.append(aux)
        case "%":
            a = stack.pop()
            aux = stack.pop() + " % " + a
            stack.append(aux)
        case "^":
            a = stack.pop()
            aux = stack.pop() + " ^ " + a
            stack.append(aux)

visualizer("110 + ( 20 - ( 30 * ( 40 / ( 50 + ( 60 ^ 2 ) ) ) ) )")

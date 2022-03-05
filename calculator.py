# This is an optional project for Formal Languages and Automata Theory 2021-2022.
# Done by Stegeran Darius Cosmin
from tabulate import tabulate

stack = []

def readfrominput(exp):
    expression = [x for x in exp.split(" ")]
    operator = []
    operator_value = {"+": 1, "-": 1, "*": 2, "/": 2, "(": 0, ")": 0, "^": 3, "%": 2}
    final = []
    for token in expression:
        auxiliary = []
        if token.isdigit():
            stack.append(int(token))
        elif token == "(":
            operator.append(token)
        elif token == ")":
            while operator and operator[-1] != "(":
                calculator(operator[-1])
                operator.pop()
            operator.pop()
        else:
            while len(operator) and operator_value[operator[-1]] >= operator_value[token]:
                calculator(operator[-1])
                operator.pop()
            operator.append(token)
        auxiliary.append(token)
        auxiliary.append(" ".join(operator))
        auxiliary.append(" ".join([str(x) for x in stack]))
        final.append(auxiliary)
    while len(operator):
        auxiliary = []
        calculator(operator[-1])
        operator.pop()
        if operator:
            auxiliary.append(operator[-1])
            auxiliary.append(" ".join(operator))
            auxiliary.append(" ".join([str(x) for x in stack]))
            final.append(auxiliary)
        else:
            auxiliary.append(" ")
            auxiliary.append("Result is: ")
            auxiliary.append(str(stack))
            final.append(auxiliary)

    print(tabulate(final, headers = ["Token", "Operator Stack", "Evaluation Stack"], tablefmt="grid"))

def calculator(exp):
    match exp:
        case "+":
            aux = stack.pop() + stack.pop()
            stack.append(aux)
        case "-":
            aux = stack.pop() - stack.pop()
            stack.append(aux)
        case "*":
            aux = stack.pop() * stack.pop()
            stack.append(aux)
        case "/":
            aux = stack.pop() / stack.pop()
            stack.append(float("{:.2f}".format(aux)))
        case "%":
            aux = stack.pop() % stack.pop()
            stack.append(aux)
        case "^":
            a = stack.pop()
            b = stack.pop()
            if b < 0:
                aux = -b ** a
            else:
                aux = b ** a
            stack.append(float("{:.2f}".format(aux)))



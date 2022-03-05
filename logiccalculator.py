# This is an optional project for Formal Languages and Automata Theory 2021-2022.
# Done by Stegeran Darius Cosmin1
from tabulate import tabulate

stack = []

def visualizer(exp):
    expression = [x for x in exp.split(" ")]
    operator = []
    operator_value = {"!": 3, "|": 1, "&": 2, "-": 2, "(": 0, ")": 0, "=": 2}
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
            aux = "("+stack.pop()+")"
            stack.append(aux)
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
            y = " ".join([str(x) for x in stack])
            auxiliary.append(y)
            final.append(auxiliary)

    print(tabulate(final, headers = ["Token", "Operator Stack", "Evaluation Stack"], tablefmt="grid"))

def calculator(exp):
    match exp:
        case "!":
            a = stack.pop()
            stack.append(neg(a))
        case "|":
            a = lor(stack.pop(), stack.pop())
            print(a)
            stack.append(a)
        case "&":
            aux = stack.pop() or stack.pop()
            stack.append(aux)
        case "-":
            aux = stack.pop() or stack.pop()
            stack.append(aux)
        case "=":
            a = equal(stack.pop(), stack.pop())
            stack.append(a)

def neg(a):
    if a == 1:
        return 0
    return 1

def lor(a,b):
    if a == 0 and b == 0:
        return 0
    return 1

def equal(a,b):
    if a == b:
        return 1
    return 0
visualizer("0 | 1 = 1")



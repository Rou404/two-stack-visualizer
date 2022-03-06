# This is an optional project for Formal Languages and Automata Theory 2021-2022.
# Done by Stegeran Darius Cosmin
from tabulate import tabulate

stack = []
final = []

def tableformer(token, operator):
    auxiliary = []
    auxiliary.append(token)
    auxiliary.append(" ".join(operator))
    auxiliary.append(" ".join([str(x) for x in stack]))
    final.append(auxiliary)

def neg(a):
    if a == 1:
        return 0
    return 1

def lor(a,b):
    if a == 0 and b == 0:
        return 0
    return 1

def land(a ,b):
    if a or b:
        return 1
    return 0

def lto(a ,b):
    if a == 0 and b:
        return 0
    return 1

def equal(a,b):
    if a == b:
        return 1
    return 0

def valuecalculator(exp):
    match exp:
        case "!":
            a = stack.pop()
            stack.append(neg(a))
        case "|":
            a = lor(stack.pop(), stack.pop())
            stack.append(a)
        case "&":
            a = land(stack.pop(), stack.pop())
            stack.append(a)
        case "-":
            a = lto(stack.pop(), stack.pop())
            stack.append(a)
        case "=":
            a = equal(stack.pop(), stack.pop())
            stack.append(a)

def calculator(exp):
    expression = [x for x in exp.split(" ")]
    operator = []
    operator_value = {"!": 3, "|": 1, "&": 2, "-": 2, "(": 0, ")": 0, "=": 2}
    for token in expression:
        if token.isdigit():
            stack.append(int(token))
        elif token == "(":
            operator.append(token)
        elif token == ")":
            while operator and operator[-1] != "(":
                tableformer(token, operator)
                valuecalculator(operator[-1])
                operator.pop()
                token = " "
            tableformer(" ", operator)
            operator.pop()

        else:
            while len(operator) and operator_value[operator[-1]] >= operator_value[token]:
                valuecalculator(operator[-1])
                operator.pop()
            operator.append(token)
        tableformer(token, operator)
    while len(operator):
        auxiliary = []
        valuecalculator(operator[-1])
        operator.pop()
        if operator:
            tableformer(operator[-1], operator)
        else:
            auxiliary.append(" ")
            auxiliary.append("Result is: ")
            y = " ".join([str(x) for x in stack])
            auxiliary.append(y)
            final.append(auxiliary)

    print(tabulate(final, headers = ["Token", "Operator Stack", "Evaluation Stack"], tablefmt="grid"))

calculator("! ( 1 | 0 ) & ! 1 | 0 - ( 1 = 1 )")



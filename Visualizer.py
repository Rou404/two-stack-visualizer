# This is an optional project for Formal Languages and Automata Theory 2021-2022.
# Done by Stegeran Darius Cosmin
from tabulate import tabulate

expression = [x for x in "A * ( F % B ^ ( C / E ) )".split(" ")]
operator = []
stack = []
operator_value = {"+": 1, "-": 1, "*": 2, "/": 2, "(": 0, ")": 0, "^": 3, "%": 2}
print(expression)
auxiliary = []
final = []

def readfrominput(expression):
    for token in expression:
        auxiliary = []
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

readfrominput(expression)


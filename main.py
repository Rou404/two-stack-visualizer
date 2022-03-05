# This is an optional project for Formal Languages and Automata Theory 2021-2022.
# Done by Stegeran Darius Cosmin
from tabulate import tabulate

expression = [x for x in "1 + 2 * ( 3 + 5 )".split(" ")]
operator = []
stack = []
operator_value = {"+": 1, "-": 1, "*": 2, "/": 2, "(": 0, ")": 0}
print(expression)
auxiliary = []
final = []
def readfrominput(expression):
    for token in expression:
        print(token, "\n")
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
                calculator(token)
            operator.append(token)
        auxiliary.append(token)
        auxiliary.append(" ".join(operator))
        auxiliary.append(" ".join(stack))
        final.append(auxiliary)
    while len(operator):
        calculator(operator[-1])
        operator.pop()
        auxiliary.append(operator[-1])
        auxiliary.append(" ".join(operator))
        auxiliary.append(" ".join(stack))
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
            if a < 0:
                aux = -a ** b
            else:
                aux = a ** b
            stack.append(float("{:.2f}".format(aux)))


readfrominput(expression)


# This is an optional project for Formal Languages and Automata Theory 2021-2022.
# Done by Stegeran Darius Cosmin

expression = [x for x in input()]
expression = expression[::-1]
operator = []
evaluation = []
operator_value = {"+": 1, "-": 1, "*": 2, "/": 2}
current = 0

print(expression)
print("token     operators        evaluation")
while expression:
    x = expression.pop()
    if x.isdigit():
        evaluation.append(x)
    elif operator_value[x] > current:
        operator.append(x)
        current = operator_value[x]
    else:
        operator.append(x)
        operator[len(operator)-2] = "("+str(x)+")"
        print("things should happen")
        #evaluation.insert(max(index for index, item in enumerate(operator) if item == x) - 1, x)

    print(str(x)+"           |   "+" | ".join(operator)+"                |   "+" | ".join(evaluation))


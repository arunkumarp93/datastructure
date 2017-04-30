def postfixEval(postfixexp):
    opStack = []
    tokenlist = postfixexp.split()

    for token in tokenlist:
        if token in "0123456789":
            opStack.append(int(token))
        else:
            op2 = opStack.pop()
            op1 = opStack.pop()
            result = doMath(token,op1,op2)
            opStack.append(result)
    return opStack.pop()



def doMath(op,op1,op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2

print(postfixEval('7 8 + 3 2 + /'))

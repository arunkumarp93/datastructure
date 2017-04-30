def infixToPostfix(token):
    opStack = []
    prec={}
    prec["*"]=3
    prec["/"]=3
    prec["+"]=2
    prec["-"]=2
    prec["("]=1
    postfix=[]
    tokenlist = token.split()

    for token in tokenlist:
        if token.isalpha() or token.isdigit():
            postfix.append(token)
        elif token == "(":
            opStack.append(token)
        elif token == ")":
            toptoken = opStack.pop()
            while toptoken != "(":
                postfix.append(toptoken)
                toptoken = opStack.pop()
        else:
            if len(opStack) == 0:
                pass
            else:
                peek = opStack[len(opStack)-1]

            while not len(opStack) == 0 and (prec[peek] >= prec[token]):
                postfix.append(opStack.pop())
            opStack.append(token)
    while not len(opStack) == 0:
        postfix.append(opStack.pop())
    return "".join(postfix)




#print(infixToPostfix("A * B + C * D"))
print(infixToPostfix("( A + B ) * C - ( D - E ) * ( F + G )"))

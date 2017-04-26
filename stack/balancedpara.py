"""find the parentheses closed properly
stack used to slove the problem
add the parenthes "(" and remove until the list length becomes zero
"""

""" python list can be used as the stack
need to use append instead of push"""
def findpara(symbolString):
    s = []
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol == '(':
            s.append(symbol)
        else:
            if len(s) == 0:
                balanced = False
            else:
                s.pop()
        index = index + 1
    if balanced and len(s)==0:
        return True
    else:
        return False
print (findpara('(())'))
print (findpara('(()'))

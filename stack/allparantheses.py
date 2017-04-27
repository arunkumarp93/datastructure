def findpara(symbolString):
    s = []
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in '([{':
            s.append(symbol)
        else:
            if len(s) == 0:
                balanced = False
            else:
                top = s.pop()
                """find the matches of open and close symbol
                 and return true if it matches"""

                if not matches(top,symbol):
                    balanced = False
        index = index + 1
    if balanced and len(s)==0:
        return True
    else:
        return False

def matches(open,close):
    opens = "([{"
    closers = ")]}"
    return opens.index(open) == closers.index(close)
print(findpara('{([])}'))
print(findpara('[{()]'))

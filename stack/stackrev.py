from stack import Stack
def revstring(mystr):
    #return mystr[::-1]
    s = Stack()
    revstr = ''
    for ch in mystr:
        s.push(ch)

    while not s.isEmpty():
        revstr = revstr + s.pop()
    print(revstr)

revstring('apple')

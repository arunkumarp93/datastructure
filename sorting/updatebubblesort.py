"""
Updated bubble sort if no exchage than exchange
becomes false then loop stop
"""
def updatedbubblesort(alist):
     passnum = len(alist)-1 # if passnum in len(alist) then it goes to list index out of bound
    exchange = True

    while passnum>0 and exchange:
        exchange = False
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                exchange = True
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
        passnum = passnum + 1
list = [2,3,5,4,8,7,6]
updatedbubblesort(list)
print (list)

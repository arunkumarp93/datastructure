"""
bubblesort check each value
one by one and if value is higher it
move it
"""
"""
It's waste of the time to check the order list that is not
going to swap
"""
def bubblesort(alist):
    length = len(alist)
    """
     find the range the list and give the
     passnum for the inner loop
     passnum = 6
    """
    for passnum in range(length-1,0,-1):
        """
          Until the range passnum it check the list
          and swap the numbers
          eg:- passnum = 6
          start from 0 to 5 loop run and check the list
         
           if range is equal to length passnum start from 0 
           and can't check whole list
           so passnum length has to decrease from higher
        """
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
list = [2,3,5,4,8,7,6]
bubblesort(list)
print(list)

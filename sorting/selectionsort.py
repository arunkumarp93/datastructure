"""
 It's works like Bubble sort
 but take the maximum and check
 with other values in the list

 Swap at the end after the complete check

"""
def selection(alist):
    length = len(alist)
    for passnum in range(length-1,0,-1):
        maximumnum = 0
        for i in range(passnum):
            if alist[i] > alist[maximumnum]:
                maximumnum = i
        temp = alist[maximumnum]
        alist[maximumnum] = alist[i]
        alist[i] = temp
un_list = [2,3,4,7,6,5,8]
selection(un_list)
print (un_list)

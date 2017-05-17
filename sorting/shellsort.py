"""
Shell short divide the list into half and apply insertion sort

"""
def shellSort(alist):
    """
    divide the list into half
    """
    sublist = len(alist) // 2
    while sublist > 0:
        #pass the value to insertsort and apply sorting
        for startpos in range(sublist):
           insertsort(alist,startpos,sublist)
        print("After increment of size",sublist,
                            "The list is",alist)
        sublist = sublist // 2

def insertsort(alist,start,gap):
    """
    insertion sort from half of the list
    sublist moves the value from start value
    e.g:- sublist = 4
    start = 0 + 4 => 4
    so
    range(4,9,4)
    next loop move to 4 to 8
    range(8,9,4)

    """
    for i in range(start+gap,len(alist),gap):

        currentvalue = alist[i]
        position = i

        """
        first check the pos 0  and pos 4
        second check pos 4 and pos 8
        """
        while position>=gap and alist[position-gap]>currentvalue:
            alist[position] = alist[position-gap]
            position = position -gap

        alist[position] = currentvalue

alist = [54,26,93,17,77,31,44,55,20]
shellSort(alist)
print(alist)

"""
Quicksort takes the pivot value and check
leftmark and rightmark value and moves
until sort

It dosen't create nex list like merge sort
"""
def quickSort(alist):
    """
    pass the value to the quicksort helper to
    split the value if rightmark < leftmark

    then recursively to quicksort for splitted list
    """
    #first = 0
    #last = len(alist)-1
    quicksorthelper(alist,0,len(alist)-1)

def quicksorthelper(alist,first,last):
    if first < last:
        # intiall splitpoint finder
        splitpoint = partition(alist,first,last)
        #recursive call after the splitpoint
        quicksorthelper(alist,first,splitpoint-1)
        quicksorthelper(alist,splitpoint+1,last)

def partition(alist,first,last):
    pivot = alist[first]
    leftmark = first + 1
    rightmark = last

    done = False

    while not done:
        """
        if leftmark value is less than pivot move the leftmark position(increase)

        if rightmark value is greater than pivot move the rightmark poistion (decrease)
        """
        while leftmark <= rightmark and alist[leftmark] <= pivot:
            leftmark = leftmark + 1
        while rightmark >= leftmark  and alist[rightmark] >=pivot:
            rightmark = rightmark - 1
        #if rightmark is less than leftmark stop looping and swap the pivot value
        if rightmark < leftmark:
            done = True
        else:
            """
             if condition fail move the rightmark to leftmark position
            """
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp
    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp

    # after sort return rightmark to splitpoint and split the list and do sort again
    return rightmark

alist = [54,26,93,17,77,31,44,55,20]
quickSort(alist)
print(alist)

"""
 choose the pivot value in the median
"""

"""
def quickSort(alist):
   quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
   if first<last:

       splitpoint = partition(alist,first,last)

       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)

def median(a,b,c):
    if ( a - b) * (c - a) >= 0:
        return a

    elif (b - a) * (c - b) >= 0:
        return b

    else:
        return c


def partition(alist,first,last):
   middle = last // 2

   pivotvalue = median(alist[first],alist[last],alist[middle])

   leftmark = first
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp

   return rightmark
"""

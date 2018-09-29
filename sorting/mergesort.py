def mergesort_helper(alist):

    list_length = len(alist)
    
    if list_length > 1:
        """
        split the list until it becomes
        to 1 uing recursive mergeSort(left),mergeSort(right)
        """
        
        """
            To run algorithm in best case O(n log n) we need to pass the
            start and end of the list instead of slice
            start = 0
            end = len(alist)
            alist[start:mid]
            alist[mid:end]
        """

        mid = list_length // 2
        start = 0
        end = list_length
        lefthalf = alist[start:mid]
        righthalf = alist[mid:end]
                
        mergesort_helper(lefthalf)
        mergesort_helper(righthalf)
    
        leftcount=0
        rightcount=0
        mergecount=0
        
        """
            compare the left and right values and add minimum
            value to the un_list[mcount] then increase the mcount position
            check the left seprate and right seprate and add to
            un_list[mcount]
        """
        leftlength = len(lefthalf)
        rightlength = len(righthalf)
        while leftcount < leftlength and rightcount < rightlength:
            if lefthalf[leftcount] < righthalf[rightcount]:
                alist[mergecount] = lefthalf[leftcount]
                leftcount += 1
            else:
                alist[mergecount] = righthalf[rightcount]
                rightcount += 1
            mergecount += 1
                
        while leftcount < leftlength:
            alist[mergecount] = lefthalf[leftcount]
            leftcount += 1
            mergecount += 1
        
        while rightcount < rightlength:
            alist[mergecount] = righthalf[rightcount]
            rightcount += 1
            mergecount += 1

def mergesort(unsorted):
    print (mergesort_helper(unsorted))


mergesort([12,55,34,66,45,99,100,1,23])

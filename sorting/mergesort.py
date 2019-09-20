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
            def mergeSort(Arr, start, end) {

	            if(start < end) :
		            mid = (start + end) / 2
		            mergeSort(Arr, start, mid)
		            mergeSort(Arr, mid+1, end)
		            merge(Arr, start, mid, end)
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
                
	"""Some cases we left with either left or right side with elements . we need to add those to merge array
 	  e.g., left = [5] and right =[5]
	  above loop add the left to merge array and failed now right array value we need to add to merge array so below 
	  loops does that work
	"""
        while leftcount < leftlength:
            alist[mergecount] = lefthalf[leftcount]
            leftcount += 1
            mergecount += 1
        
        while rightcount < rightlength:
            alist[mergecount] = righthalf[rightcount]
            rightcount += 1
            mergecount += 1
    return alist
    
def mergesort(unsorted):
    print (mergesort_helper(unsorted))


mergesort([12,55,34,66,45,99,100,1,23])

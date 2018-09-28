def mergesort_helper(un_list):

    list_length = len(un_list)
	
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

        mid = list_length// 2
		start = 0
		end = len(un_list)
        lefthalf = un_list[start:mid]
        righthalf = un_list[mid:end]
				
        mergesort_helper(lefthalf)
        mergesort_helper(righthalf)
    
        lcount=0
        rcount=0
        mcount=0
		
		"""
			compare the left and right values and add minimum
			value to the un_list[mcount] then increase the mcount position
			check the left seprate and right seprate and add to
			un_list[mcount]
		"""
        while lcount < len(lefthalf) and rcount < len(righthalf):
            if lefthalf[lcount] < righthalf[rcount]:
                un_list[mcount] = lefthalf[lcount]
                lcount = lcount + 1
            else:
                un_list[mcount] = righthalf[rcount]
                rcount = rcount + 1
            mcount = mcount + 1
                
        while lcount < len(lefthalf):
            un_list[mcount] = lefthalf[lcount]
            lcount = lcount+1
            mcount = mcount + 1
        
        while rcount < len(righthalf):
            un_list[mcount] = righthalf[rcount]
            rcount = rcount + 1
            mcount = mcount+1

def mergesort(unsorted):
    print (mergesort_helper(unsorted))


mergesort([12,34,55,21,45,99,100,1,23])

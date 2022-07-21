
def merge(left, right):
    """
    Arguments:
    --------------------
    left[list]: left array
    right[list]: right array
    
    return merge[list]
    --------------------
    
    Check the right and left of the element and continuously and
    add values to temp array
    
    if any values remaining in left or right of the array
    will added separately by checking left and right
    
    [10] [5]
    
    first loop checks the and add 10 to temp. Now 5 is left
    it'll be added by right loop
    
    """
    temp = []
    leftindex = 0
    rightindex = 0
    
    leftlength = len(left)
    rightlength = len(right)
    
    while leftindex < leftlength and rightindex < rightlength:
        leftvalue = left[leftindex]
        rightvalue = right[rightindex]
        if leftvalue < rightvalue:
            temp.append(leftvalue)
            leftindex += 1
        else:
            temp.append(rightvalue)
            rightindex += 1
    
    while leftindex < leftlength:
        temp.append(left[leftindex])
        leftindex += 1
    
    while rightindex < rightlength:
        temp.append(right[rightindex])
        rightindex += 1
        
    return temp  
    
def divider(array, start, end):
    """
    Arguments:
    ----------------------
    array[list]: list of elements to merge
    start[int]: starting value of list
    end[int]: ending value of list
    ----------------------
    
    Split the array until one element
    [1,2,3,4]-->
    [1,2] [3,4]
    [1] [2] [3] [4]
    
    Then pass the left and right of the array to merge
    """
    if len(array)  > 1:
        mid = len(array)//2
        left  = array[0:mid]
        right = array[mid:end]
        sorted_left = divider(left, start, mid)
        sorted_right = divider(right, mid+1, end)
        return merge(sorted_left, sorted_right)
    else:
	# return array so it'll be added to sorted variable and pass to merge 
	# and get sorted list 
        return array
        
    """
        Alternative code of above
        if len(array) <= 1:
            return array
        
        mid = len(array)//2
        left  = array[0:mid]
        right = array[mid:end]
        sorted_left = divider(left, start, mid)
        sorted_right = divider(right, mid+1, end)
        return merge(sorted_left, sorted_right)
        
    """



def mergesort(array):
    divider(array, 0, len(array))
    
mergesort([10,5,4,11,3,8,2,1])

# Merge Sort Bottom UP:
# merge with temporary array and copy the sorted values to array again.

def merger_with_temp_array(array, temp, left, mid, end):
    left_count = left
    right_count = mid
    key = left
    
    while left_count<mid and right_count< end:
        if array[left_count] < array[right_count]:
            temp[key] = array[left_count]
            left_count += 1
        else:
            temp[key] = array[right_count]
            right_count += 1
        key += 1
    
    while left_count < mid and left_count < len(array):
        temp[key] = array[left_count]
        left_count += 1
        key += 1
    
    for move_key in range(left, end):
        array[move_key] = temp[move_key]
    
            
            
def merge_sort(array):
    
    current = 1
    len_array = len(array)
    left = 0
    
    temp = array.copy()
    
    while current < len_array: 
        left = 0
        while left < len_array:
            mid = min(left+current, len_array)
            
            right = min(left + current*2, len_array)
            
            merger_with_temp_array(array, temp, left, mid, right)
            
            left = left + current * 2
        
        current = 2 * current
        
print(merge_sort([4, 2, 3, 1, 6, 5]))

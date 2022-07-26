def sort_helper(array, left, right):
    """
    Move the element less than pivot to left pointer.
    If there is no element then move the pivot to the left pointer.
    
    return the left pointer index 
    """
    left_marker = left
    pivot = array[right]
    
    for i in range(left, right):
        if array[i] <= pivot:
            array[i], array[left_marker] = array[left_marker], array[i]
            left_marker += 1
            
    array[left_marker], array[right] = array[right], array[left_marker]
            
    return left_marker
    
def quick_sort(array, left, right):
    """
      Sort until the left is less than right.
      
      find the mid value in first sort then do it continuosly to half of the array
      every sort left side array end in mid - 1 and right side array start from mid + 1 
      since mid sorted already.
    """
    if left < right:
        
        mid = sort_helper(array, left, right)
            
        quick_sort(array, left, mid-1)
        quick_sort(array, mid+1, right)
    
data = [8, 7, 2, 1, 0, 9, 6]
data = [12,3,4,5,0,8,2,11,7]
quick_sort(data, 0, len(data)-1)

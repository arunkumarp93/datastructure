def mergeSort(alist):
    length = len(alist)
    print("Splitting ",alist)
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
    if length > 1:
        mid = length // 2
        left = alist[:mid]
        right = alist[mid:]

        mergeSort(left)
        mergeSort(right)

        i=0
        j=0
        k=0

        """
        compare the left and right values and add minimum
        value to the alist[k] then increase the k position

        check the left seprate and right seprate and add to
        alist[k]
        """
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                alist[k] = left[i]
                i= i + 1
            else:
                alist[k] = right[j]
                j=j+1
            k = k + 1
        while i < len(left):
            alist[k] = left[i]
            i = i + 1
            k = k + 1
        while j < len(right):
            alist[k] = right[j]
            j=j+1
            k=k+1

    print("Merging ",alist)

alist = [54,26,93,17,77,31,44,55,20]
mergeSort(alist)
print(alist)

from heap.heap import Heap


def heapsort(a):
    """
     heapsort fetch the top value and add to sorted part of the list

     Ascending order:
     create min heap
     remove the top
     Added to end of the list

     Descing order:
     create max heap
     remove the top
     Added to end of the list

    """
    heapds= Heap()
    # build min heap
    heapds.build_heap(a)
    # heap sort ascending order
    size = heapds.get_current_size()
    for i in range(size):
        removed_value = heapds.remove()
        heapds.heaplist.append(removed_value)
    return heapds.get_heap()

 heapsort([10,5,4,9,2,3,4])

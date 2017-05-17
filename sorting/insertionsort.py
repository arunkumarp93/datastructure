"""
 Insertion sort BIG O O(n^2)
 But in different way

 take position 0 is already sorted and
 sort the values based on the first value

 if postion 0 is greater tha postion in swap
 right to left and make the postion value as next
"""
def insertionsort(alist):
    for index in range(1,len(alist)):
        currentvalue = alist[index]

        position = index
        """
        check the poistion 0 and position 1
        if pos0 < pos1 loop skim and currentvalue change
        """
        """
         position 2 is lower than postion 1 swap it to position 1
         now continuosly check the position 0 and position 1
         current value still position 2

         if postion 0 is higher than pos1 then it swap pos1 to pos0
        """
        while position > 0 and alist[position-1] > currentvalue:
            """
            swap the current position to previous
            and decrease postion value
            """
            alist[position] = alist[position-1]
            position = position - 1
        alist[position] = currentvalue
list = [2,3,5,4,8,7,6]
insertionsort(list)
print (list)

class Heap:
    """
     Heap ADT

     An array based data structure visualized like a nearly
     a complete binary tree.

     Tree to list conversion:

     Initially we need to store the empty value
     To manage tree struture in array list To get the left, Right
     and parent of node we need to use below calculations

     Note (i = current position)

     Left --> i * 2
     Right --> i * 2  + 1
     parent --> i // 2

     Public access methods:

     insert(value)
     remove()
     build_heap(values)

    """
    def __init__(self):

       self.heaplist = [0]
       self.current_size = 0
       self.type = None

    def get_left_child(self, i):
       return 2 * i

    def get_right_child(self, i):
      return 2 * i + 1

    def get_parent(self, i):
       return i // 2

    def find_heap_violation(self, position):
       """
       find the minimum or maximum cild of left and right

       then return the minimum/maximum node position

       If heap type is none min heap condition will be checked
       by default
       """
       left = self.get_left_child(position)
       right = self.get_right_child(position)

       if right > self.current_size:
           return left

       if self.type == 'max':
           if self.heaplist[left] < self.heaplist[right]:
               return right
           else:
               return left
       else:
           if self.heaplist[left] < self.heaplist[right]:
               return left
           else:
               return right

    def child_swap(self, node_position, child_position):
       # swap helper for validate children
       if self.type == 'max':
           if self.heaplist[node_position] < self.heaplist[child_position]:
               self.heaplist[node_position], self.heaplist[child_position] = \
                            self.heaplist[child_position] , self.heaplist[node_position]

       else:
            if self.heaplist[node_position] > self.heaplist[child_position]:
                self.heaplist[node_position], self.heaplist[child_position] = \
                self.heaplist[child_position] , self.heaplist[node_position]


    def parent_swap(self, node_position, parent_position):
        # swap helper for validate parents

        if self.type == 'max':
             if self.heaplist[node_position] > self.heaplist[parent_position]:
                 self.heaplist[node_position], self.heaplist[parent_position] = \
                         self.heaplist[parent_position], self.heaplist[node_position]

        else:
            if self.heaplist[node_position] < self.heaplist[parent_position]:
                 self.heaplist[node_position], self.heaplist[parent_position] = \
                 self.heaplist[parent_position], self.heaplist[node_position]

    def validate_children(self, i):
       """
         validate the left and right child of the node

         args: i node position
       """
       while i * 2 <= self.current_size:
            child_node_position = self.find_heap_violation(i)
            self.child_swap(i , child_node_position)
            i = child_node_position

    def validate_parents(self, i):
       """
       validate parent element
       """
       parent = self.get_parent(i)
       while parent > 0:
          self.parent_swap(i, parent)
          i = parent
          parent = self.get_parent(parent)


    def insert(self, value):
       """
       insert at end of the list and validate the parent
       """
       self.heaplist.append(value)
       self.current_size += 1
       self.validate_parents(self.current_size)

    def remove(self, value = None):
       """
        If value given
        Naive search take O(n) time
        need to implement in hash table method

        If no value:
          swap the top element with last element
          remove the last element
          Update the heap_size
          validate the childrens

       """
       removed_value = self.heaplist[1]
       self.heaplist[1] = self.heaplist[self.current_size]
       self.heaplist.pop(self.current_size)
       self.current_size += -1
       self.validate_children(1)
       return removed_value


    def build_heap(self, values, max = False):
       """
       default min heap will be created

       """
       if max:
           self.type = 'max'
       else:
           self.type = 'min'
       length = len(values) // 2
       self.heaplist = [0] + values
       self.current_size = len(values)
       while length > 0:
            self.validate_children(length)
            length = length - 1

    def __str__(self):
        return '-->'.join(str(v) for v in self.heaplist[1:])

    def get_current_size(self):
        return self.current_size

    def get_heap(self):
        return self.heaplist[1:]

heap = Heap()

print("*"*150)
print('Max heap sample')
heap.build_heap([10, 9, 1, 2, 4], max)
print("After build heap", heap)
heap.insert(0)
print("After insert", heap)
heap.remove()
print("After remove first element", heap)

print("*"*75)
print('Min heap sample')
heap.build_heap([10, 9, 1, 2, 4])
print("After build heap", heap)
heap.insert(0)
print("After insert ", heap)
heap.remove()
print("After remove first element", heap)

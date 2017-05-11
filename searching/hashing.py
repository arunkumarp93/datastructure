class Hashfind:
    def __init__(self,tablesize):
        self.size = tablesize
        self.slots = [None] * self.size
        self.data = [None] * self.size
    """
    use self if the function is not define global
    and if it it inside the class

    """
    def put(self,key,data):
        hashvalue = self.hashfunction(key,len(self.slots))

        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            nextslot = rehash(hashvalue,len(self.slots))
            while self.slots[nextslot] != None and\
                    self.slots[nextslots] != key:
                nextslot = rehash(nextslot, len(self.slots))
            if self.slots[nextslot] == None:
                self.slots[nextslot] = key
                self.data[nextslot] = data
            else:
                self.data[nextslot] = data

"""
  startslot find using hashfunction

  find the position and check the position value
  in the self.data[position]
"""
    def get(self,key):
        startslot = self.hashfunction(key,len(self.slots))

        data = None
        stop = False
        found = None
        position = startslot

        while self.slots[position] != None and \
                        not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(self,position,len(self.slots))
                if position == startslot:
                    stop = True

    def hashfunction(self,key,size):
        return key%size
    def rehash(self,oldhash,size):
        return (oldhash+1)%size

    def __getitem__(self,key):
        self.get(key)
    """
    To set the value in poistion we need __setitem__
    """
    def __setitem__(self,key,data):
        self.put(key,data)

tablesize = 11
h = Hashfind(tablesize)
h[20] = 24
h[34] = 11
h[54] = "cat"

"""
__getitem__ get the value from the hash
"""
print(h[54])

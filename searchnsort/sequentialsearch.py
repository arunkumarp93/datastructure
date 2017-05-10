"""
search each value in the list
and return if value found
"""

def sequentialsearch(list,searchvalue):
    length = len(list)
    found = False
    pos = 0
    while pos < length and not found:
        if list[pos] == searchvalue:
            found = True
        else:
            pos = pos + 1

testlist = [1,2,3,4,7,8,9,6]
sequentialsearch(testlist,6)

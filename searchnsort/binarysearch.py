"""
 Binary search has to do after the sort
"""
def bssearch(slist,searchvalue):
    first = 0
    midvalue = len(slist) // 2
    """
    check midvalue is searchvalue
    also check after the slicing
    """
    if slist[midvalue] == searchvalue:
        return True
    else:
        if slist[midvalue] > searchvalue:
            """
                slice the list and recursive call the bssearch()
                new list created based on midvalue if search item
                is Greater than  midvalue then
                slice create the list before midvalue
            """
            return bssearch(slist[:midvalue],searchvalue)
            """
                    slice the list and recursive call the bssearch()
                    new list created based on midvalue if search item
                    is less than  midvalue then
                    slice and create the list after midvalue
            """
        elif slist[midvalue] < searchvalue:
            return bssearch(slist[midvalue+1:],searchvalue)
sortedlist = [1,3,5,6,7,8,10,13,15]
bssearch(sortedlist,10)

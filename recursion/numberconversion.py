"""
Recursion has the three rules
1) should have base case
condition to quit the process
2) change the state and move to base case again
call the base class after change
3) should call the base class continuously
"""
#base case
def conversion(n,base):
    convertstring = "0123456789ABCDEF"
    #condition for base case
    if n < base:
        return convertstring[n]
    else:
        #condition 2 & 3 (change the state and call the base case)
        return conversion(n//base,base) + convertstring[n%base]
conversion(5,2)

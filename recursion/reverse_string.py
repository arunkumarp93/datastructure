"""
Reverse the string using Recursion
1) base condition string length should be gt 0
2) to change the state remove the s[0] fromthe string
and concat it to s
To remove the first letter s[1:]

after the complete string remove it will return the
s in reverse like stack pop so "hello" will return as
"o","l","l","e","h"

"""
def reverse(s):
    length = len(s)
    if length <=0:
        return s
    else:
        return reverse(s[1:]) + s[0]

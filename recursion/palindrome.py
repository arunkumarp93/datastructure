"""
find the palindrome remove the space,
special character using isalphanum
then  find the palindrome

"""
import re
def isalphanum(s):
    return re.sub('[^a-zA-Z0-9]+', '',s)

def removeWhite(s):
    if s=="":
        return s
    else:
        return removeWhite(s[1:]) + s[0]

def isPal(s):
    if s == removeWhite(s):
        return True
    else:
        return False
print isPal(isalphanum("madam i'm adam"))

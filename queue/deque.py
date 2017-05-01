from collections import deque
"""
python ADT has deque in collection
To import the element rightside
append(value)
leftside
appendleft(value)
popleft
popleft()
popright
pop()
"""
def palindrome(string):
    findpal = deque(string)
    print deque(reversed(findpal))
    stillEqual = True
    while len(findpal) > 1 and stillEqual:
        front = findpal.pop()
        rear = findpal.popleft()
        if front != rear:
            stillEqual = False
    return stillEqual

palindrome("lsdkjfskf")
palindrome("radar")

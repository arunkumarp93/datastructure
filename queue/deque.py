from collections import deque
"""
python ADT has deque in collection
To insert the element:
rightside
append(value)
leftside
appendleft(value)

To remove element:
popleft
popleft()
popright
pop()


"""
def palindrome(string):
    findpal = deque(string)
    stillEqual = True
    while len(findpal) > 1 and stillEqual:
        front = findpal.pop()
        rear = findpal.popleft()
        if front != rear:
            stillEqual = False
    return stillEqual

palindrome("lsdkjfskf")
palindrome("radar")

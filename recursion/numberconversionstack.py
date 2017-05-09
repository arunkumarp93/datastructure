"""
  implement the stack and append the remainder
  instead of concat to string everytime
"""
s=[]
def conversion(n,base):
    convertstring = "01234567890ABCDEF"
    if n < base:
        return s.append(convertstring[n])
    else:
        s.append(convertstring[n%base])
        conversion(n//base,base)
    convert = ""
    while len(s) > 0:
        convert = convert + str(s.pop())
    return convert


conversion(10,2)

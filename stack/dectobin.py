def dectobin(number):
    s = []

    while number > 0:
        rem = number % 2
        s.append(rem)
        number = number // 2

    binary = ""

    while len(s) > 0:
        binary = binary + str(s.pop())
    print binary

dectobin(5)

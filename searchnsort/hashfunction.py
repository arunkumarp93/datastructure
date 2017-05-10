"""
Has table also called hash function
that store the values in slot

Each hash position of table is called slot

It takes the values and return them in integer of
hash length

Eg:

Below hash function have 11 position to calucate the hash

value for alphabet we have to use ASCII values of the char e.g ord('a')

find the all chars ascii and sum them finally modolo the sum with hash function length

we can find the hash value for alphabet
eg:-

cat ascii calue is 312
len of table is 11
312 % 11 = 4

cat pos in table is 4

"""

def hash(astring,table):
    sum = 0
    t_length = len(table)
    for pos in range(len(astring)):
        sum = sum + ord(astring[pos])
    table_pos = sum % t_length
    table[table_pos] = astring
    return table_pos
table = [None] * 11
hash("cat",table)

"""
To find the hash value for anagram string
multiply ascii value with position
eg :-
ord('a') = 99
position = 2
sum = 99 * 2

below example find the hash value for anagaram string

"""

def hash(astring,table):
    sum = 0
    t_length = len(table)
    for pos in range(len(astring)):
        ascii_value =  ord(astring[pos])
        sum = sum + ascii_value * (pos + 1)
    table_pos = sum % t_length
    table[table_pos] = astring
    return table_pos
table = [None] * 11
hash("cat",table)

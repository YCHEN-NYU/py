# parse a bunch of strings by characters except a -> z, A -> Z
# .split() can only work with ASCII
testStr = '''There are several different variations of the 8-bit ASCII table. The table below is according to ISO 8859-1, also called ISO Latin-1. Codes 128-159 contain the Microsoft Windows Latin-1 extended characters.'''
strList = list(testStr)
print "Length of List = ", len(strList)
print strList

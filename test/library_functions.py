__author__ = 'narendra'

print abs(-5) # 5
print abs(5) # 5

print "*******************************************************"

def all(iterable):
    for element in iterable:
        if not element:
            return False
    return True
iterable_a = [1,2,3,4,5,'']
print all(iterable_a) # False

def any(iterable):
    for element in iterable:
        if element:
            return True
    return False
iterable_a = [1,2,3,4,5,'']
print any(iterable_a) # True

print "*******************************************************"

print chr(65)  # A

print cmp(2,4) # -1 x < y
print cmp(2,2) # 0  x == y
print cmp(6,4) # 1  x > y

'''
divmod(a, b) = (a // b, a % b)
'''
print divmod(4, 2) # (2, 0)

print "*******************************************************"

'''
Enumerate =

def enumerate(sequence, start=0):
    n = start
    for elem in sequence:
        yield n, elem
        n += 1

'''
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
print list( enumerate(seasons) )  # [(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
print list( enumerate(seasons, start=1) )  # [(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]


x = 1
print eval('x+2') # 3

'''
Filter
filter(function, iterable) == [item for item in iterable if function(item)]
'''
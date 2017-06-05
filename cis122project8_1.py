"""
CIS 122 Spring 2017 Project8_1
Author: Yin Jin
Description: loop, examples
"""
import doctest
#(0)
def diff_first_last(L):
    '''
    (list) -> boolean
    
    Precondition: len(L) >= 2
    Returns True if the first item of the list is different from the last;
    else returns False.
    
    >>> diff_first_last([3, 4, 2, 8, 3])
    False
    >>> diff_first_last(['apple', 'banana', 'pear'])
    True
    >>> diff_first_last([4.0, 4.5])
    True
    >>> diff_first_last(['pear'])        ##borderline example
    False
    >>> diff_first_last([])              ##borderline example
    '''
    if len(L) == 0:
        return None
    return not(L[0] == L[len(L)-1])

#(0)(b)
def middle(L):
    '''
    (list)-> number or str

    returns the item in the middle position of L,
    when L has an odd length.
    Otherwise, middle should return 999999.

    >>> middle ([2,5,4,7,0])
    4
    >>> middle ([2,5,7,4])
    999999
    >>> middle ([1,'f','r',5,'d'])
    'r'
    >>> middle (['d'])
    'd'
    >>> middle ([])
    'please enter a list'
    '''
    if len(L) == 0:
        return 'please enter a list'
    l = len(L)//2
    if len(L) % 2 == 0:
        return 999999
    else:
        return L[l]
#(2)
def mySum(L):
    '''
     L, a list of numbers.
     mySum returns the sum of the numbers in the input list.

     >>> mySum ([2,3,2])
     7
     >>> mySum ([])
     0
     >>> mySum ([2])
     2
     '''
    s = 0
    for i in L:
        s+=i
    return s        


    

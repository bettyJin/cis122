'''
CIS 122 Spring 2017 Project6-2
Author: Yin Jin
Descipyion: using for, while loops: DNAtranscribe to RNA and finding the double amount for de 
'''
import doctest

#(0)
#(a)
def checklen (astring, le):
    '''
    (str,int)->bool

    checklen has two parameters, astring, of type string and le, an integer,
    that returns True if astring is at least le characters long,
    and False otherwise.

    >>> checklen ("abc",3)
    True
    >>> checklen ("djaf",1)
    False
    '''
    return len(astring) == le

#(b)
def is_nonalnum (astring):
    '''
    (str)->bool

    takes one input parameter, astring, of type string and
    returns True if astring contains at least one non-alphanumeric character,
    and False otherwise.

    >>> is_nonalnum("#cbnaej")
    True
    >>> is_nonalnum('vjkjdvkdn')
    False
    '''

    return not(str.isalnum(astring))

#(c)
def is_noEe (astring):
    '''    
    (str)-> bool

    is_noEe takes one input parameter, astring, of type string and
    returns True if astring does NOT contain the characters 'E' or 'e',
    and False otherwise.

    >>> is_noEe('aehre')
    True
    >>> is_noEe('aEsh')
    True
    >>> is_noEe('afhwt')
    False
    '''
    r = False
    i = 0
    while i<len(astring) and r == False:
        if astring[i] == 'e':
           r = True
        elif astring[i] =='E':
           r = True
        else:
            r = False
        i+=1
    return r

#(d)
def is_uc_alpha (astring):
    '''
    (sring)-> bool
    is_uc_alpha, with one parameter, astring,
    returns True if any character in astring is an uppercase letter,
    and returns False otherwise.

    >>> is_uc_alpha('Udsnvjka')
    True
    >>> is_uc_alpha('dasgsdg')
    False
    '''

    r = False
    i = 0
    while i<len(astring) and r == False:
        if str.isupper( astring[i] ) == True:
            r = True
        else:
            r = False
        i+=1
    return r

#(e)
def is_2numbers (astring):
    '''
    (str) -> bool

     is_2numbers, with one parameter, astring,
     returns True if astring has at least two numbers,
     and otherwise returns False

    >>> is_2numbers ('aer3erh5')
    True
    >>> is_2numbers ('aer3er')
    False
    >>> is_2numbers ('aererh')
    False
    '''
    r=0
    for i in astring:
        if str.isdigit(i) == True:
            r+=1
        else:
            r=r

    if r>=2:
        return True
    else:
        return False


#(f)
def is_special_char (astring):
    '''
    (str)-> bool

    is_special_char, with one parameter, astring,
    which returns True if astring contains any of the special characters,
    '!', '@', '#', '$', '%', '^', '&',
    and otherwise returns False.

    >>> is_special_char ("qjrbe@jsdbv")
    True
    >>> is_special_char ('!@#$%^&')
    True
    >>> is_special_char ('jdnsjk')
    False
    '''
    r=0
    for i in astring:
        if i == '!':
            r+=1
        elif i == '@':
            r+=1
        elif i == '#':
            r+=1
        elif i == '$':
            r+=1
        elif i == '%':
            r+=1
        elif i == '^':
            r+=1
        elif i == '&':
            r+=1
        else:
            r=r
    if r>0:
        return True
    else:
        return False

#(Challenge)
    
def countdownBy2(n):
    '''
    (int)->None

    countdownBy2 counts down by 2 from n and prints 'Blastoff',

    >>> countdownBy2(3)
    3
    1
    Blastoff
    >>> countdownBy2(8)
    8
    6
    4
    2
    0
    Blastoff
    '''
    while n >= 0:
        print(n)
        n-=2
            
    print('Blastoff')
    return None    


     

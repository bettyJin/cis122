'''
CIS 122 Spring 2017 Project5_1
Author: Yin Jin
Descipyion: practice with Python Boolean data type and conditional statements
            and fubction return values           
'''
import doctest

#(0)
#(a) 
def isbn_gendigit (isbn):           
    '''(string)->None

    find the last digit of ISBN
    
    >>> isbn_gendigit('068333923')
    0683339230   
    >>> isbn_gendigit('020131452')
    0201314525
    >>> isbn_gendigit('020141452')
    020141452X
    '''
    s=0
    for i in range(0,9):
        a=isbn[-i-1]
        a=int(a)
        m=a*(i+2)
        s=s+m                   
    
    r = 11 - s % 11

    if r == 11:
        print(isbn + "0")
    elif r ==10:
        print(isbn+"X")       
    else:
        print(isbn+str(r))
    return None

#(1)
import doctest
def is_safelead(lead,ball,time):
    '''
    (int,boolean,number)->boolean

    Implement the "safe lead" algorithm, designed by sportswriter Bill James,
    which is designed to answer the question, Under what conditions can you
    safely determine that a lead in a basketball game is insurmountable?
    lead, the number of points by which one team is ahead;
    ball, True if the team that is ahead has the ball and False otherwise;
    time, the number of seconds left in the game. 

    >>> is_safelead(20,True,180)
    True
    >>> is_safelead(10,False,100)
    False
    '''
    point = lead - 3
    
    if ball== True:
        p = point + 0.5
    else: 
        p = point - 0.5
        
    p=p*p
    return p>time


#(Challenge)
def isbn_gendigit2 (isbn):           
    '''(string)->None

    find the last digit of ISBN
    
    >>> isbn_gendigit2('068333923')
    '0683339230'   
    >>> isbn_gendigit2('020131452')
    '0201314525'
    >>> isbn_gendigit2('020141452')
    '020141452X'
    '''
    s=0
    for i in range(0,9):
        a=isbn[-i-1]
        a=int(a)
        m=a*(i+2)
        s=s+m                   
    
    r = 11 - s % 11

    if r == 11:
        new_isbn = isbn + "0"
    elif r ==10:
        new_isbn = isbn+"X"       
    else:
        new_isbn = isbn+str(r)
    return new_isbn

def isbn_check(isbn):
    '''
    (string)-> bool

    determines whethertheISBNiswell-formedTh.

    >>> isbn_check('097522980X')
    True
    >>> isbn_check('0681319216')
    True
    >>> isbn_check('5678901230')
    True
    >>> isbn_check('5678901231')
    False
    '''
    
    nine_isbn = isbn[0:9]
    right_isbn = isbn_gendigit2(nine_isbn)
    return isbn == right_isbn













    




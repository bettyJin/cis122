'''
CIS 122 Spring 2017 Project4-2
Author: Yin Jin
Descipyion: 
'''
#(0)(a)
def max_trans1 (a,b,c):
    '''(number)->None

    find maximum weight that can be transported along this road
    
    >>> max_trans1(1,2,3)
    1
    '''
    m=min(a,b,c)
    print(m)
    return None

#(0)(b)
def max_trans2 (a,b,c,d,e):
    '''(number)->None

    find maximum weight that can be transported along this road
    
    >>> max_trans1(1,2,3,4,5)
    4
    '''
    m1=min(a,b,c)
    m2=min(d,e)
    m3=max(m1,m2)
    print(m3)
    return None

#(1)
def isbn_gendigit (isbn):           ##"020131452"
    '''(string)->None

    find the last digit of ISBN
    
    >>>isbn_gendigit('020131452')
    0201314525   
    '''
    s=0
    for i in range(1,10):
        a=isbn[i-1]
        a=int(a)
        m=a*i
        s=s+m                       ##115
        
    r=11-(s%11)                     ##11-5=6
    
    for n in range (0,10):
        x=(n*10)%11                 ##(5*10)%11=6
        c=x-r                       ##6-6=0
        if c==0:
            print(isbn+str(n))
    return None



### (challenge)
### not any 9-digit code can be found the last digit number.
### for example 123456789 doesn't work
### the example that I found is 0000000019; 0000010006; 0001000004










'''
CIS 122 Spring 2017 Project4-1
Author: Yin Jin
Descipyion: 
'''

from turtle import*
speed('fastest')
#(0)
def spiral (side):
    '''(integer) -> None

    Draws a spiral with right turns and
    lines up to the length specified in side.

    >>> side(100)
    '''
    for sidelen in range(1, side+1, 5):
        forward(sidelen)
        right(90)
    return None

def spiral2 (side):
    '''(integer) -> None

    Draws a spiral with increase angle turn and
    lines up to the length specified in side.
    
    >>> side(100)
    '''
    for sidelen in range(1, side+1, 5):
        forward(sidelen)
        right(sidelen)
    return None

def spiral3 (side, angle):
    '''(integer) -> None
    
    Draws a spiral with set angle turns and
    lines up to the length specified in side.

    >>> side(100,90)
    '''
    for sidelen in range(1, side+1, 5):
        forward(sidelen)
        right(angle)

    return None



#(1)

#(1a)
def poly (n,le):
    '''(int, number)->Nome
    
    draw an n-sided polygon with sides of length le and color polor

    >>>poly (3,100)    
    '''
    for a in range (1,n+1):
        fd(le)
        lt(360/n)

    return None

#(1b)
def poly (n,le,pcolor):
    '''(int, number, string)->Nome
    
    draw an n-sided polygon with sides of length le and color polor

    >>>poly (3,100, "yellow")
    '''
    color(pcolor,pcolor)
    begin_fill()
    for a in range (1,n+1):
        fd(le)
        lt(360/n)

    end_fill()
    return None

#(1c)
def house ():
    """
    ()->None    

    using three polygon to draw a house

    >>>house()    
    """

    poly (3,300,"red")
    penup()
    setposition(0,-300)
    pendown()
    poly (4,300,"brown")
    penup()
    setposition(100,-300)
    pendown()
    poly(4,100,"green")  

    return None

##(challenge)
from turtle import*
#c
pu()
setposition(-250,50)
pd()
circle(100,-180)
#I
pu()
setposition(-210,50)
pd()
lt(180)
fd(70)
bk(35)
lt(90)
fd(200)
lt(90)
fd(35)
bk(70)
#S
pu()
setposition(-80,50)
pd()
left(180)
circle(50,-40)
circle(50,220)
lt(180)
circle(50,-220)
#1
pu()
setposition(50,50)
pd()
setheading(90)
fd(190)
#2
pu()
setposition(190,50)
pd()
lt(90)
fd(80)
goto(190,200)
lt(270)
circle(40,180)
#2
pu()
setposition(290,50)
pd()
setheading(180)
fd(80)
goto(290,200)
rt(90)
circle(40,180)
#Y
pu()
setposition(-350,-50)
pd()
goto(-300,-100)
goto(-250,-50)
goto(-300,-100)
setheading(270)
fd(120)
#I
pu()
setposition(-230,-230)
pd()
setheading(0)
fd(70)
bk(35)
lt(90)
fd(180)
lt(90)
fd(35)
bk(70)
#N
pu()
setposition(-130,-230)
pd()
setheading(90)
fd(180)
goto(-50,-230)
goto(-50,-50)
#J
pu()
setposition(20,-50)
pd()
setheading(0)
fd(80)
bk(40)
lt(90)
bk(140)
circle(30,-180)
#I
pu()
setposition(110,-230)
pd()
setheading(0)
fd(70)
bk(35)
lt(90)
fd(180)
lt(90)
fd(35)
bk(70)
#N
pu()
setposition(290,-230)
pd()
setheading(90)
fd(180)
goto(210,-230)
goto(210,-50)










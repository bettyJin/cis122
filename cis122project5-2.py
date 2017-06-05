'''
CIS 122 Spring 2017 Project5_2
Author: Yin Jin
Descipyion:          
'''
from turtle import*
import random
import doctest

#(0)
def mars_explore_main():
    '''
    () -> None
    Main function for mars_explore
    sets up print and graphical
    output and then calls mars_explore.

    Calls: mars_explore
    >>> mars_explore_main()
    '''
    # label print output
    print('xpos', '\t',
'ypos', '\t', 'water', '\t', 'temp')
    
    # set up for graphical output
    reset(); hideturtle()
    title('Mars Rover')
    display_color = 'blue'
    color(display_color)
    
    # draw the rover
    dot(10, display_color)
    
    # explore twenty places on Mars
    for _ in range(20):
        mars_explore()
        
    return None

#(1a)
def rover_loc ():
    '''
    () -> int
    return random number for rover location
    >>> rover_loc()
    125
    '''
    r=random.randint(-250,250)
    return r

def water_content():
    '''
    () -> int
    return random number for water content
    >>> water_content()
    100
    '''
    w=random.randint(1,290)
    return w

def temp():
    '''
    () -> int
    return random number for temp
    >>> temp()
    -134
    '''
    t=random.randint(-178,1)
    return t

#(1b)
d_color='blue'
def mars_explore():
    '''
    ()->None
    draw the path that robet move on the mars
    >>> mars_explore()
    '''
    x=rover_loc()
    y=rover_loc()
    goto(x,y)
    dot(10, d_color)
    w = water_content()
    t = temp()
    print(x,'\t', y, '\t', w , '\t', t)
    return None
















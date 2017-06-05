'''
CIS 122 Spring 2017 Project3_1
Author: Yin Jin
Descipyion: draw a square and atriangle by using turtle and for loops
'''
from turtle import*


#1(a)

c=input('color of the square')

speed(9)
color(c)

for a in range(4):
    fd(100)
    lt(90)


#1(b)
c=input('color of the square')

speed(9)
color(c)

for a in range(3):
    fd(100)
    lt(120)

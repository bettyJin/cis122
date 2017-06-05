'''
CIS 122 Spring 2017 Project3_2
Author: Yin Jin
Descipyion: Art show by useing turtle
'''
from turtle import*
speed('fastest')

a=0
b=0
c=250
r=100
colormode(255)


for a in range(120):
    tup = (a, b, c)
    pencolor(tup)
    for i in range(4):
        fd(r)
        lt(90)
    lt(3)
    a+=2

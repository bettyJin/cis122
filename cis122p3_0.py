'''
CIS 122 Spring 2017 Project3_0
Author: Yin Jin
Descipyion: sun and the earth
'''
from turtle import*

r = 2.7
e = r
s = 109 * r # sun to earth ratio

speed(0)
color("blue",'blue')
penup()
setposition(-300,-300)
pendown()
begin_fill()
circle(r)
end_fill()


begin_fill()
color('yellow')
penup()
setposition(0,-290)
pendown()
circle(s)
end_fill()

"""
CIS 122 Spring 2017 Project1:Hello, Python
Author: Yin Jin
Description: cost of t-shirt;color skittles; minutes in a year
"""

#1
ttl_shirts=128
ttl_green=ttl_shirts//2
ttl_yellow=ttl_shirts-ttl_green
cost_green=15
ttl_green_cost=ttl_green*cost_green
cost_yellow=10
ttl_yellow_cost=ttl_yellow*cost_yellow
ttl_cost=ttl_yellow_cost+ttl_green_cost
print(ttl_cost)

ttl_shirts=129
ttl_green=ttl_shirts//2
ttl_yellow=ttl_shirts-ttl_green
cost_green=15
ttl_green_cost=ttl_green*cost_green
cost_yellow=10
ttl_yellow_cost=ttl_yellow*cost_yellow
ttl_cost=ttl_yellow_cost+ttl_green_cost
print(ttl_cost)

#2
a=7
Or=a
G=3*Or
P=Or+G
R=P//2
Y=100-Or-G-P-R
print(Or)
print(G)
print(P)
print(R)
print(Y)

a=6
Or=a
G=3*Or
P=Or+G
R=P//2
Y=100-Or-G-P-R
print(Or)
print(G)
print(P)
print(R)
print(Y)

#3
m=1
h=60*m
day=24*h
year=365*day
print(year)





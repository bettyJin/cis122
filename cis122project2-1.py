'''
CIS 122 Spring 2017 Project2-1
Author: Yin Jin
Descipyion: practice about built-in functon, string, print/input/, andforloop
'''
#(0)tip calculator
a=input("Please ennter total bill?: ")
a=float(a)
tip15=round(a*0.15,2)
b=str(tip15)
tip18=round(a*0.18,2)
c=str(tip18)
tip20= round(a*0.2,2)
d=str(tip20)
print("suggested tip at 15% is $"+b+'.')
print("suggested tip at 18% is $"+c+'.')
print("suggested tip at 20% is $"+d+'.')

#(1) Fancy Name Display
name=input('Please enter your name: ')
l=len(name)+4
print('*'*l)
print('*',name,'*')
print('*'*l)

#(2) Double-len
a=input('Please input string to check: ')
count=0
for b in a:
    count+=1
print('Length of input string: ', count)
print('Python length for input string: ',len(a))

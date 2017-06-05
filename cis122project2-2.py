'''
CIS 122 Spring 2017 Project2-2
Author: Yin Jin
Descipyion: practice about built-in functon, string, print/input, and for loop
'''
#(0) Mixups
a=input("Please enter some text: ")
d=""
for b in a:
    c=b+b
    d=d+c
print("Double string:",d)
print("Letter reverse string:",a[len(a)-1]+a[1:len(a)-1]+a[0])


#(1)Greeting
name=input("Please enter a name: ")
print("Hello,", name[0:]+'!')

#(2)Stamps for Sale
amount = input('Please give a whole dollar amount for stamps: ')
amount = int(amount)
card = amount * 100 // 34
print("Post card stamps:", card)
penny = amount *100 % 34
print("Penny stamps:", penny)

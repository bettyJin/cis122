'''
CIS 122 Spring 2017 Project7_1
Author: Yin Jin
Descipyion: Rock, Paper, Scissors (stop the function when i told it to do so)
'''
#(0)
import random
def rps():
    '''
    ()->None

     implements the game Rock, Paper, Scissors.
     Each of two players is asked for their selection,
     and the function prints out which player wins.
     ask a player whether they would like to play the other game
     
     >>> rps()
    '''
    i = 1
    while i == 1:
        s1 = random.choice('rps')
        s2 = random.choice('rps')
        if s1 == s2:
            winner = 'tie'
        elif s1 == 'r':
            if s2 == 'p':
                winner = 'side2'
            else:
                winner = 'side1'
        elif s1 == 'p':
            if s2 == 's':
                winner = 'side2'
            else:
                winner = 'side1'
        else:
            if s2 == 'r':
                winner = 'side2'
            else:
                winner = 'side1'
        print ('side1 is',s1)
        print ('side2 is',s2)
        print ('winner is',winner )
                
        b=input('Do you want to play again (Yes or No):')
        if b== 'No':
            i = 2



            
    

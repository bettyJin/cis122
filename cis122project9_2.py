'''
CIS 122 Spring 2017 Project9-2
Author: Yin Jin
Descipyion: file
'''
from cis122project9_1 import *
def fbkup (fname):
    '''
    (str)-> None

    with one parameter, fname,
    the name of a text (.txt) file.
    fbkup will create a backup for file fname,
    with the name <fname>-bkup.txt.
    fbkup should return the name of the new backup file.

    >>> fbkup('week.txt')
    '''
    
    newf = fname[:len(fname)-4] + '-bkup.txt'
    
    
    with open (fname, 'r') as f:
        with open (newf, 'w') as n:
            for line in f:
                n.write(line)
    return newf

           
check_file('week.txt')
print()
mybackupf = fbkup('week.txt')
check_file(mybackupf) 

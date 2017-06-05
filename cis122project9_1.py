'''
CIS 122 Spring 2017 Project9-1
Author: Yin Jin
Descipyion: file
'''
def check_file(fname):
    '''
    (str)->None

    parameter, fname, the name of a file.
    check_file should open file fname,
    and print the contents of the file line by line,
    just as it appears in the file.
    None value is returned.

    >>> check_file('project9.txt')
    Monday
    Tuesday
    Wednesday
    Thursday
    Friday
    Saturday Sunday
    '''
    with open(fname) as f:
        f=f.readlines()
        for i in f:
            print (i,end='')
    return None


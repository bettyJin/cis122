'''
CIS 122 Spring 2017 Project8_2
Author: Yin Jin
Descipyion:
'''
import doctest
from cis122project6_2 import *

#(1)
def frequent (psw):
    '''
    (str) -> bool

    If psw is in a list of frequently used passwords
    ('password', '12345', 'qwerty', 'letmein', 'trustno1', '000000', 'passw0rd'),
    frequent should return False;
    otherwise, return True.

    >>> frequent ('12345')
    False
    >>> frequent ('')
    True
    >>> frequent ('jink')
    True
    '''
    f_psw = ['password', '12345', 'qwerty', 'letmein', 'trustno1', '000000', 'passw0rd']
    for chr in f_psw:
        if psw == chr:
            return False
    return True
#
def passwordChecker(paw):
    '''
    >>> passwordChecker('000000')
    False
    >>> passwordChecker('#Qwerty')
    False
    >>> passwordChecker('#qwErty')
    False
    >>> passwordChecker('#Qw9rty')
    False
    >>> passwordChecker('#Qw99rty')
    True
    >>> passwordChecker('12345')
    False
    >>> passwordChecker('A99!')
    False
    >>> passwordChecker('Abyz9!')
    False
    >>> passwordChecker('qwerty99!')
    False
    >>> passwordChecker('Qwerty99')
    False
    '''
    if len(paw) < 5:
        return False

    if not(is_uc_alpha(paw)):
        return False
    
    if not(is_2numbers(paw)):
        return False

    if is_noEe(paw):
        return False

    if not(is_special_char(paw)):
        return False

    f_paw = ['password', '12345', 'qwerty', 'letmein',
             'trustno1','000000', 'passw0rd']
    if paw in f_paw:
        return False

    return True

        

    

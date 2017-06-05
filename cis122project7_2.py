'''
CIS 122 Spring 2017 Project7_2
Author: Yin Jin
Descipyion:  simple input, normal input, boundary input, e.g., 0, 1, empty strings, etc.
'''
import doctest
def count_vowels(s):
    '''
    (str) -> int
    Return number of vowels(aeiou) in s.

    >>> count_vowels('The quick brown fox')
    5
    >>> count_vowels('')
    0
    >>> count_vowels('dgy')
    0
    >>> count_vowels('I love U')
    4
    '''
    vowels = 'aeiouAEIOU'    ### also count capital letter
    ctr = 0
    for ch in s:
        if ch in vowels:
            ctr += 1         ### unify the name

    return ctr

#(1)
def find_min_and_max(values):
    '''
    (string) -> None

    Find the maximum and minimum values in a non-empty string of digits
    and print them. None value is returned.

    >>> find_min_and_max('jm12')   ### earlier example 
    The minimum value is 1
    The maximum value is 2
    >>> find_min_and_max('428')
    The minimum value is 2
    The maximum value is 8
    >>> find_min_and_max('1234567890')
    The minimum value is 0
    The maximum value is 9
    >>> find_min_and_max('5')
    The minimum value is 5
    The maximum value is 5
    
    '''
    mmin = 10                        ## we are try to find the min so we need to set up a largest number between 0 to 9
    mmax = 0
    for value in values:
        if str.isdigit(value):       ### we only whan to compare numbers 
            value = int (value)      ### need to change 'value' to a number to compare
            if value > mmax:
                mmax = value
            if value < mmin:
                mmin = value
    print('The minimum value is', mmin)
    print('The maximum value is', mmax)

    #or
    #print('The minimum value is {}'.format(mmin))
    #print('The maximum value is {}'.format(mmax))

    return None
#(2)
def my_average(dataset):
    '''(string) -> float
    returns average of values in input string values,
    but zeros do not count at all
    no usable data, return 0

    >>> my_average('23')
    2.5
    >>> my_average('203')
    2.5
    >>> my_average('00000000')
    0
    >>> my_average('3')
    3.0
    '''
    count = 0
    total = 0
    for value in dataset:
        if value != '0':
            total += int(value)
            count += 1                 ### position was woring

    if count == 0:                     ### no usable data, return 0
        return 0
    else:
        return total / count

# (3)
def minutesToHours(minutes):
    '''(number) -> float

    convert input minutes to hours;
    return hours

    >>> minutesToHours(60)
    1.0
    >>> minutesToHours(90)
    1.5
    >>> minutesToHours(0)
    0.0
    '''
    hours = minutes / 60
    hours = round(hours, 2)
    # print(hours)                 
    return hours                 ### we don't need to print, need return

def hoursToDays(hours):
    '''
    (number) -> float
    convert input hours to days;
    return days

    >>> hoursToDays(24)
    1.0
    >>> hoursToDays(100)
    4.17            
    >>> hoursToDays(0)
    0.0
    '''
    days = round(hours / 24, 2)           ### only want two digits after decimal point according to the example 
    return days

def daysToYears(days):
    '''
    (number) -> float
    convert input days to years;
    return years
    >>> daysToYears(365)
    1.0
    >>> daysToYears(100)
    0.27
    >>> daysToYears(0)
    0.0
    '''
    ### days = 365                       ### no need for this line, if we do so we will only return 1
    years = days / 365
    years = round(years, 2)
    return years

def minutesToYears(m):
    '''
    (int) -> float
    
    input number m minutes is converted to equivalent number of years.
    return years. call auxiliary functions to do each step.

    >>> minutesToYears(525600)
    1.0
    >>> minutesToYears(5256000)
    10.0
    >>> minutesToYears(394200)
    0.75
    >>> minutesToYears(0)
    0.0
    '''
    h = minutesToHours(m)               ### we need to creat variable h, d, y
    d = hoursToDays(h)                  ### to store and ues it later 
    y = daysToYears(d) 
    return y













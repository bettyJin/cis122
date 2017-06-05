'''
CIS 122 Spring 2017 Project6-1
Author: Yin Jin
Descipyion: using for, while loops: DNAtranscribe to RNA and finding the double amount for de 
'''
import doctest
#(0)(a)
def transcribe (s):
    '''
    (string)-> string

    a string S, which will have DNA nucleotides
    (capital letter As, C, Gs, and Ts).
    There may be other characters, too,
    though they will be ignored by the transcribe function --
    Then, transcribe should return as output the messenger RNA
    that would be produced from that string S.
    The correct output simply uses replacement:
    'A's in the input become 'U's in the output.
    'C's in the input become 'G's in the output.
    'G's in the input become 'C's in the output.
    'T's in the input become 'A's in the output.

    >>> transcribe('ACGT TGCA')
    'UGCAACGU'
    >>> transcribe('GATTACA')
    'CUAAUGU'
    >>> transcribe('GAtTtTACA')  # data may need to be cleaned up a bit
    'CUAAUGU'
    >>> transcribe('cs5')        # lowercase doesn't count
    ''
    '''
    RNA = ''
    for i in s:
        if i == 'A':
            r = 'U'
        elif i == 'C':
            r = 'G'
        elif i == 'G':
            r = 'C'
        elif i == 'T':
            r = 'A'
        else:
            r = ''
        RNA += r
    return RNA

#(b)
def transcribe (s):
    '''
    (string)-> string

    a string S, which will have DNA nucleotides
    (capital letter As, C, Gs, and Ts).
    There may be other characters, too,
    though they will be ignored by the transcribe function --
    Then, transcribe should return as output the messenger RNA
    that would be produced from that string S.
    The correct output simply uses replacement:
    'A's in the input become 'U's in the output.
    'C's in the input become 'G's in the output.
    'G's in the input become 'C's in the output.
    'T's in the input become 'A's in the output.

    >>> transcribe('ACGT TGCA')
    'UGCAACGU'
    >>> transcribe('GATTACA')
    'CUAAUGU'
    >>> transcribe('GAtTtTACA')  # data may need to be cleaned up a bit
    'CUAAUGU'
    >>> transcribe('cs5')        # lowercase doesn't count
    ''
    '''
    
    RNA = ''
    a = 0
    while a<len(s):
        i = s[a]
        if i == 'A':
            r = 'U'
        elif i == 'C':
            r = 'G'
        elif i == 'G':
            r = 'C'
        elif i == 'T':
            r = 'A'
        else:
            r = ''
        RNA += r
        a+=1
    return RNA

### in this case, for loop is better than while loops,
### because computer do a lot of work for us in for loops.

#(1)
def savings (deposit, rate):
    '''
    (num,num)-> num
    with two parameters, deposit and rate,
    that returns the number of years it will take for an initial
    deposit to a savings account to double, if it grows at rate (rate).
    Print the initial deposit and
    the amount in the savings account at the end of each year

    >>> savings(50,0.5)
    initial deposit: 50
    amount at 1 year: 75.0
    amount at 2 year: 112.5
    2
    >>> savings(100,0.1)
    initial deposit: 100
    amount at 1 year: 110.0
    amount at 2 year: 121.0
    amount at 3 year: 133.1
    amount at 4 year: 146.41
    amount at 5 year: 161.05
    amount at 6 year: 177.16
    amount at 7 year: 194.87
    amount at 8 year: 214.36
    8
    '''
    n=0
    initial_d = deposit
    print('initial deposit:', initial_d)
    while deposit < 2 * initial_d:
        deposit = deposit * (1 + rate)
        n+=1
        print('amount at', n, 'year:', round(deposit,2))

    return n


        

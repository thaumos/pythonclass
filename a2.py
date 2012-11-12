def get_length(dna):
    ''' (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    '''

    return (len (dna))

def is_longer(dna1, dna2):
    ''' (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    '''

    if get_length(dna1) > get_length(dna2):
        return True
    else:
        return False

def count_nucleotides(dna, nucleotide):
    ''' (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    '''

    num_nucleotide = 0

    for char in dna:
        if char in nucleotide:
            num_nucleotide = num_nucleotide + 1

    return num_nucleotide


def contains_sequence(dna1, dna2):
    ''' (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False
    
    '''
    if dna2 in dna1:
       return True
    else:
        return False

def is_valid_sequence(dna):
    ''' (str) -> bool

    Return True if and only if the nucleotides
    in the sequence are valid.

    >>> is_valid_sequence('ATCGTCA')
    True
    >>> is_valid_sequence('ATCGRNA')
    False

    '''

    dna == 'ATCG'

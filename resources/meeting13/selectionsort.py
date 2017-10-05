"""
# Selection sort method, aka insertion sort
Source: Lee & Hubbard (2015). "Data Structures and Algorithms with Python"
http://knuth.luther.edu/~leekent/CS2Plus/chap4/chap4.html
"""

def select(seq, start):
    minIndex = start

    for i in range(start+1, len(seq)):
        if seq[minIndex] > seq[i]:
            minIndex = i

    return minIndex

def selectionSort(seq):
    for i in range(len(seq)-1):
        minIndex = select(seq, i)
        tmp = seq[i]
        seq[i] = seq[minIndex]
        seq[minIndex] = tmp

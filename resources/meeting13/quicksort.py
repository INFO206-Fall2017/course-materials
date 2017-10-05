"""
# Quick sort method
Source: Lee & Hubbard (2015). "Data Structures and Algorithms with Python"
http://knuth.luther.edu/~leekent/CS2Plus/chap4/chap4.html
"""

import random

def partition(seq, start, stop):
    pivotIndex = start
    pivot = seq[pivotIndex]

    i = start+1
    j = stop-1

    while i <= j:
        while i <= j and not pivot < seq[i]:
            i+=1
        while i <= j and pivot < seq[j]:
            j-=1

        if i < j:
            tmp = seq[i]
            seq[i] = seq[j]
            seq[j] = tmp
            i+=1
            j-=1

    seq[pivotIndex] = seq[j]
    seq[j] = pivot

    return j


def quicksortRecursively(seq, start, stop):
    if start >= stop-1:
        return 

    pivotIndex = partition(seq, start, stop)

    quicksortRecursively(seq, start, pivotIndex)

    quicksortRecursively(seq, pivotIndex+1, stop)

def quicksort(seq):
	# randomize the sequence first
	for i in xrange(len(seq)):
		j = random.randint(0,len(seq)-1)
		tmp = seq[i]
		seq[i] = seq[j]
		seq[j] = temp

    quicksortRecursively(seq, 0, len(seq))


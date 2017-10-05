"""
# Merge sort method
Source: Lee & Hubbard (2015). "Data Structures and Algorithms with Python"
http://knuth.luther.edu/~leekent/CS2Plus/chap4/chap4.html
"""

def merge(seq, start, mid, stop):
    lst = []
    i = start
    j = mid

    # Merge the two lists while each has more elements
    while i < mid and j < stop:
        if seq[i] < seq[j]:
            lst.append(seq[i])
            i+=1
        else:
            lst.append(seq[j])
            j+=1

    # Copy in the rest of the start to mid sequence    
    while i < mid:
        lst.append(seq[i])
        i+=1

    # # Copy in the rest of the mid to stop sequence
    # # Optional code
    # while j < mid:
    #     lst.append(seq[j])
    #     j+=1

    # Copy the elements back to the original sequence   
    for i in range(len(lst)):
        seq[start+i]=lst[i]

def mergeSortRecursively(seq, start, stop):
    # We must use >= here only when the sequence we are sorting
    # is empty. Otherwise start == stop-1 in the base case.
    if start >= stop-1:
        return 

    mid = (start + stop) // 2

    mergeSortRecursively(seq, start, mid)
    mergeSortRecursively(seq, mid, stop)
    merge(seq, start, mid, stop)

def mergeSort(seq):
    mergeSortRecursively(seq, 0, len(seq))                     

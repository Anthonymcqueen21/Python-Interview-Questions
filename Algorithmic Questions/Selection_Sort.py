# Sorting uses in-place comparison
# Time complexity: 0(n**2)
# Space Complexity: 0(1) Auxilary
# Stable

"""
Takes a list of integers and sorts them in ascending order. This sorted
list is then returned.
"""

# Implementation

def sort(seq):
    for i in range(0, len(seq)):
       iMin = i
       for j in range(i+1, len(seq)):
          if seq[iMin] > seq[j]:
             iMin = j
       if i != iMin:
          seq[i], seq[iMin] = seq[iMin], seq[i]
    return seq
   

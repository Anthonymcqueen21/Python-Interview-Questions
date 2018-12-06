# Quick Sort uses partitioning to recursively divide and sort the list
# Time Complexity: 0(n**2) worst case
# Space Complexity: 0(n**2) this version

"""
Takes a list of integers and sorts them in ascending order. This sorted
list is then returned.
"""
def sort(seq):
    if len(seq) <= 1:
       return seq
    else:
       pivot = seq[0]
       left, right = [], []
       for x in seq[1:]:
           if x < pivot:
              left.append(x)
           else:
              right.append(x)
       return sort(left) + [pivot] + sort(right)

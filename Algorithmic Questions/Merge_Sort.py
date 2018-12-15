# Uses divide and conquer method with recursive means
# Time Complexity: 0(n log n)
# Space Complexity: 0(n)

# Python Implementation

def merge(left, right):
    """
    Taking two sorted sub list and merges them into a single sorted sub list
    and returns it.
    """
    
    results = []
    n, m = 0, 0
    while n < len(left) and m < len(right):
       # Seeing if the left is equal or less than right
        if left[n] <= right[m]:
        # We are going to add left n
            result.append(left[n])
            # See if n is n + n = 1
            n += 1
        else:
        # We are going to add right m
            result.append(right[m])
            m += 1
            
    result += left[n:]
    result += right[m:]
    return result
    
# Now we are going to define sorting

def sort(seq):
    """
    Takes a list of integers and sorts them in asending order and returns the list.
    """
    if len(seq) <= 1:
       return seq
       
    middle = int(len(seq) / 2)
    left = sort(seq[:middle])
    right = sort(seq[middle:])
    return merge(left, right)
    
    

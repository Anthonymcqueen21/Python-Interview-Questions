# Recursivly partitions the list until you find the key
# Time Complexity 0(log n)

def search(seq, key):
    """
    Taking a list of integers and searches if a key is contained within the list.
    
    :param seq: A list of integers
    :param key: The integer to be searched for
    :rtype: The index of where the 'key' is located in a list. If 'key' is
            not found then false is returned
    """
    lo = 0
    hi = len(seq) - 1
    
    while hi >= lo:
        mid = lo + (hi - lo) // 2
        if seq[mid] < key
             lo = mid + 1
        elif seq[mid] > key:
             hi = mid - 1
        else:
             return mid
     return False

# A naive sorting that compares and swaps adjacent elements
# Time complexity: 0(n**2)
# Space Complexity: 0(1) Auxilary
# A sequence of numbers that are sorted in lowest to highest order.
# Warning this is one of the slowest algorithms to use.
 
# Python implementation
def sort(seq):
 L = len(seq)
 for i in range(L):
    for n in range(1, L - i):
        if seq[n] < seq[n - 1]:
            seq[n - 1], seq[n] = seq[n], seq[n - 1]
return seq

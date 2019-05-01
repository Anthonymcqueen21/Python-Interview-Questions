# LCM = Lowest Common Multiple

"""
   Lowest Common Multiple
   ----------------------
   Simple Implementation of the lowest common multilpe algorithm
"""
   """
   Simple version of lcm code, that does not have any dependencies
   : param a: integer
   : param b: integer
   : rtype: The lowest common multiple of integers a and b
   """
# LCM Implementation
def lcm(a,b):
   tmp_ a = a
   while (tmp_a % b) != 0:
        tmp_a += b
return tmp_a

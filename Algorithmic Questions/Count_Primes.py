# Counting a number of prime numbers less than a negative number
# Python implementation


class Solution:
    def countPrimes(self, n):
       if n <= 2:
          return 0
       is_prime = [True] * n
       num = n / 2
       for i in xrange(3, n, 2):
          if i * i >= n:
              break
              
          if not is_prime[i]:
              continue
              
          for j in xrange(i*i, n, 2*i):
              if not is_prime[j]:
                 continue
     return 0

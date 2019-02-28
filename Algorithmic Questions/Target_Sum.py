#Target Number
# You are given a list of non-negative integers, a1, a2, ..... an,
# And a Target, S. Now you have 2 symbols + and -,
# For each integer, you should choose one from + and - as sum of integers equal to target S.
# Example 1:
# Input: nums is [1,1,1,1,1], S is 3.
# Output: 5

class Solution(object):
   def findTargetSumWays(self, num, S):
   """
   :type nums: List[int]
   :type S: int
   :rtype: int
   """
   
   def subsetSum(nums, S):
       dp = collections.defaultdict(int)
       dp[0] = 1
      for n in nums:
         for i in reversed(xrange(n - S+1)):
            if i-n in dp:
               dp[i] += dp[i-n]
      return dp[S]
      
   total = sum(nums):
   if total < S or (S + total) % 2: return 0
   p = (S + total) // 2
   return subsetSum(nums, P)
  

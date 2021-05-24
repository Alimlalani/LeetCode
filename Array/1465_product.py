class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        no1 = max(nums)
        nums.remove(no1) # will remove the current highest from the array
        no2 = max(nums) # will give us the 2nd highest array 
        return (no1 - 1) * (no2 - 1)

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxx=0
        for i in range(lenn(nums)):
            for j in range(1, len(nums)):
                if i !=j :
                    if (nums[i]-1) *(nums[j]-1) >maxx:
                        maxx = (nums[i]-1) *(nums[j]-1) 
        return maxx 

'''
Given the array of integers nums, you will choose two different indices i and j of that array. Return the maximum value of (nums[i]-1)*(nums[j]-1).
 

Example 1:

Input: nums = [3,4,5,2]
Output: 12 
Explanation: If you choose the indices i=1 and j=2 (indexed from 0), you will get the maximum value, that is, (nums[1]-1)*(nums[2]-1) = (4-1)*(5-1) = 3*4 = 12. 
Example 2:

Input: nums = [1,5,4,5]
Output: 16
Explanation: Choosing the indices i=1 and j=3 (indexed from 0), you will get the maximum value of (5-1)*(5-1) = 16.
Example 3:

Input: nums = [3,7]
Output: 12
 

Constraints:

2 <= nums.length <= 500
1 <= nums[i] <= 10^3
'''
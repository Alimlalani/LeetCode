class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        
        s=0
        for i in range(len(arr)):
            for j in range(i,len(arr),2):
                s+=sum(arr[i:j+1])
        return s



'''
Input: arr = [1,2]
Output: 3
Explanation: There are only 2 subarrays of odd length, [1] and [2]. Their sum is 3.
Example 3:

Input: arr = [10,11,12]
Output: 66
'''
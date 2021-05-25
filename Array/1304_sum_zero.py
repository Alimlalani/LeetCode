class Solution:
    def sumZero(self, n: int) -> List[int]:
        ans = []
		# If n is odd, append value 0 in your returned array.
        if n%2 != 0:
            ans.append(0)
		# Return an array where the values are symmetric. (+x , -x).
        for i in range(n//2):
            ans.extend([-(i+1),(i+1)])
        return ans
        

class Solution:
    def sumZero(self, n: int) -> List[int]:
        ans=[]
        if n==1:
            return [0]
        elif n%2==0:
            for i in range(-n//2,0):
                ans.append(i)
            for i in range(1,(n//2)+1):
                ans.append(i)
            return ans
        else:
            for i in range((-n//2)+1,(n//2)+1):
                ans.append(i)
        return ans


'''

Given an integer n, return any array containing n unique integers such that they add up to 0.

 

Example 1:

Input: n = 5
Output: [-7,-1,1,3,4]
Explanation: These arrays also are accepted [-5,-1,1,2,3] , [-3,-1,2,-2,4].
Example 2:

Input: n = 3
Output: [-1,0,1]
Example 3:

Input: n = 1
Output: [0]

'''
'''

You are given a string s of even length. Split this string into two halves of equal lengths, and let a be the first half and b be the second half.

Two strings are alike if they have the same number of vowels ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'). Notice that s contains uppercase and lowercase letters.

Return true if a and b are alike. Otherwise, return false.

 

Example 1:

Input: s = "book"
Output: true
Explanation: a = "bo" and b = "ok". a has 1 vowel and b has 1 vowel. Therefore, they are alike.
Example 2:

Input: s = "textbook"
Output: false
Explanation: a = "text" and b = "book". a has 1 vowel whereas b has 2. Therefore, they are not alike.
Notice that the vowel o is counted twice.
Example 3:

Input: s = "MerryChristmas"
Output: false
Example 4:

Input: s = "AbCdEfGh"
Output: true


'''

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n=len(s)
        a=s[:n//2]
        b=s[n//2:]
        count1=0
        count2=0
        vowels=('a','e','i','o','u','A','E','I','O','U')
        for i in a:
            if i in vowels:
                count1 +=1
        for i in b:
            if i in vowels:
                count2+=1
        return(count1==count2)
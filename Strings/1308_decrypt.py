class Solution:
    def freqAlphabets(self, s: str) -> str:
        
        i=0
        output=""
        while i<len(s):
            if i<len(s)-2 and s[i+2]=="#":
                output+=chr(int(s[i:i+2])+ord("a")-1)
                i+=2
            else:
                output+=chr(int(s[i])+ord("a")-1)
            i+=1
        return output
        



'''


Given a string s formed by digits ('0' - '9') and '#' . We want to map s to English lowercase characters as follows:

Characters ('a' to 'i') are represented by ('1' to '9') respectively.
Characters ('j' to 'z') are represented by ('10#' to '26#') respectively. 
Return the string formed after mapping.

It's guaranteed that a unique mapping will always exist.

 

Example 1:

Input: s = "10#11#12"
Output: "jkab"
Explanation: "j" -> "10#" , "k" -> "11#" , "a" -> "1" , "b" -> "2".
Example 2:

Input: s = "1326#"
Output: "acz"
Example 3:

Input: s = "25#"
Output: "y"
Example 4:

Input: s = "12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#"
Output: "abcdefghijklmnopqrstuvwxyz"


''' 
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alphabets = 'abcdefghijklmnopqrstuvwxyz'
        counter = 0
        output = True
        
        for i in alphabets:
            if i in sentence:
                counter += 1
                
                if counter == 26:
                    output = True
            else:
                output = False
        
        return output

                        OR
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return len(set(sentence)) >= 26

'''

A pangram is a sentence where every letter of the English alphabet appears at least once.

Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.

 

Example 1:

Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
Output: true
Explanation: sentence contains at least one of every letter of the English alphabet.
Example 2:

Input: sentence = "leetcode"
Output: false
 

Constraints:

1 <= sentence.length <= 1000
sentence consists of lowercase English letters.

'''
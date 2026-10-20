class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        # keep a hashmap of every letter in s and t
        sLetters = {}
        tLetters = {}
        for letter in s:
            if letter in sLetters:
                sLetters[letter] += 1
            else:
                sLetters[letter] = 1
            
            
        for letter in t:
            if letter in tLetters:
                tLetters[letter] += 1
            else:
                tLetters[letter] = 1
        
        return sLetters == tLetters
        


        
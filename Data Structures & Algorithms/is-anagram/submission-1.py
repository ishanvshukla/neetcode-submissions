class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # keep a hashmap of every letter in s
        
        sLetters = {}

        for letter in s:
            if s in sLetters:
                sLetters[letter] += 1
            else:
                sLetters[letter] = 1
            
        # go through t and see if you can build it with the letters from s

        for letter in t:
            if letter not in sLetters:
                return False
            elif sLetters[letter] == 0:
                return False
            else:
                sLetters[letter] -= 1

        return True


        
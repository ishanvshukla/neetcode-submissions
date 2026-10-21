class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # keep a hashmap of every letter in s and t
        sLetters = {}
        tLetters = {}
        for letter in s:
            if s in sLetters:
                sLetters[letter] += 1
            else:
                sLetters[letter] = 1
            
            
        for letter in t:
            if t in tLetters:
                tLetters[letter] += 1
            else:
                tLetters[letter] = 1
        
        # see if you can build t with the letters from s
        for letter in t:
            if letter not in sLetters:
                return False
            else:
                sLetters[letter] -= 1
                tLetters[letter] -= 1

        return True


        
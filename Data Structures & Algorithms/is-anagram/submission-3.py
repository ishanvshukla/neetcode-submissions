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
        
        # go through t and see if you can build it with the letters from s
        for letter in t:
            # if the current letter in t doesn't exist in s, invalid anagram
            if letter not in sLetters:
                print("this t letter doesn't exist in s")
                return False
            # if we don't have any of these letters left, return 0
            
            else:
                sLetters[letter] -= 1
                tLetters[letter] -= 1

        return True


        
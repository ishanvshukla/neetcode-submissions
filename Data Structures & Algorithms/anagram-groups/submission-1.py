class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # helper function to return the hashmap of letter counts
        def getLetterCounts(string):
            letterCounts = {}
            for c in string:
                if c in letterCounts:
                    letterCounts[c] += 1
                else:
                    letterCounts[c] = 1
            return letterCounts
        # for each word, create a hashmap of letter counts for each word
        # check if the hashmap exists in our anagram tracking hashmap, because if it does, we can append

        # the overall hashmap will keep (dictionary, list) pairs
        anagrams = defaultdict(list)
        # iterate through everyword
        for string in strs:
            letters = getLetterCounts(string)
            anagrams[tuple(sorted(letters.items()))].append(string)

        # then we just need to collect each of the values and append them to our return list
        result = []
        for val in anagrams.values():
            result.append(val)
        return result

            
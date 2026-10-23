class Solution:

    def encode(self, strs: List[str]) -> str:
        # just iterate through the list and concatenate every string together
        # add a delimiter for every string, since we will need to decode it
        encoded_string = ""
        for string in strs:
            encoded_string += string + ","
        return encoded_string

    def decode(self, s: str) -> List[str]:
        # every string will end with a pound symbol so just iterate until you find that
        start = 0
        end = 0
        result = []
        while start < len(s) and end < len(s):
            # move end until we find "#"
            while s[end] != ",":
                end += 1
            # now we get the string from start to end and append
            result.append(s[start:end])
            # the new start will be right after then end
            start = end + 1
            end = start
        return result

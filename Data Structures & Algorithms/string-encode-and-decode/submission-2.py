class Solution:

    def encode(self, strs: List[str]) -> str:
        # just iterate through the list and concatenate every string together
        # append the length of each string before it, so the decoder can just 
        # slice the whole string once it finds the length
        # add the delimiter after the length
        encoded_string = ""
        for string in strs:
            encoded_string += str(len(string))+ "#" + string
        return encoded_string

    def decode(self, s: str) -> List[str]:
        # every string will end with a pound symbol so just iterate until you find that
        start = 0
        end = 0
        result = []
        while start < len(s) and end < len(s):
            # move end until we find "#"
            while s[end] != "#":
                end += 1
            # now we have the length from s[start:end]
            length = int(s[start:end])
            start = end + 1
            end = start + length
            result.append(s[start:end])
            start = end
            end = start
        return result

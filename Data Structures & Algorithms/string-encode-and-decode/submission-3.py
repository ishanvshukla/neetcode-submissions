class Solution:

    def encode(self, strs: List[str]) -> str:
        # just iterate through the list and concatenate every string together
        # append the length of each string before it, so the decoder can just 
        # slice the whole string once it finds the length
        # add the delimiter after the length
        # time complexity is O(n) because it takes linear time to add all n strings from 
        # the list to the encoded_string
        # space complexity is O(1), constant, no extra space required (not counting the encoded_string because that is auxiliary space)
        encoded_string = []
        for string in strs:
            encoded_string.append(str(len(string)) + "#" + string)
        return "".join(encoded_string)

    def decode(self, s: str) -> List[str]:
        # every string will end with a pound symbol so just iterate until you find that
        start = 0
        end = 0
        result = []
        # time complexity is O(n) to append all the strings of s to the list (n = length of s)
        # space complexity is O(1) constant, because it doesn't grow with the input size, the only extra space we use is the length, start, end variables
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

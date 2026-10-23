class Solution:

    def encode(self, strs: List[str]) -> str:
        # Prefix each string with "length#" so "#" inside strings is safe
        # Time: O(n * k), Space: O(n * k)
        pieces = []
        for string in strs:
            pieces.append(str(len(string)) + "#" + string)
        return "".join(pieces)

    def decode(self, s: str) -> List[str]:
        # Read the length up to "#", then slice that many characters
        # Time: O(m), Space: O(1) excluding output, m = len(s)
        start = 0
        end = 0
        result = []
        while start < len(s):
            while s[end] != "#":
                end += 1
            length = int(s[start:end])
            start = end + 1
            end = start + length
            result.append(s[start:end])
            start = end
        return result
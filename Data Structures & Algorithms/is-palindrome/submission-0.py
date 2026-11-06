class Solution:
    def isPalindrome(self, s: str) -> bool:
        # keep two pointers, starting at the left and right
        # if the pointer is not at an alphanumeric character, move it until it is
        # if the two pointers cross, we know the string is a palindrome
        # if they are mismatched somewhere it isn't
        left = 0
        right = len(s) - 1
        while left < right:
            # move left pointer until we find an alphanumeric character
            while not s[left].isalnum() and left < right:
                left += 1
            # move right pointer until we find an alphanumeric character
            while not s[right].isalnum() and right > left:
                right -= 1
            left_char = s[left].lower()
            right_char = s[right].lower()
            if left_char != right_char:
                return False
            left += 1
            right -= 1
        return True
        
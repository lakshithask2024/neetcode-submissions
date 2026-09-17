class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1  # two pointers

        while l < r:
            while l < r and not s[l].isalnum():  # skip non-alphanumeric left
                l += 1
            while l < r and not s[r].isalnum():  # skip non-alphanumeric right
                r -= 1

            if s[l].lower() != s[r].lower():     # compare case-insensitive
                return False

            l += 1
            r -= 1

        return True
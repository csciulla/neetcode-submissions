class Solution:
    def isPalindrome(self, s: str) -> bool:
        lower = s.lower()
        new = []
        for char in lower:
            if isinstance(char, int) or char.isalnum():
                new.append(char)
        return new == new[::-1]
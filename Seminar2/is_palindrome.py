from typing import Optional


class Solution1:
    def is_palindrome(self, s: str) -> bool:
        new_str = ""

        for c in s:
            if c.isalnum():
                new_str += c.lower()

        return new_str == new_str[::-1]


class Solution2:
    def is_palindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not self.alpha_num(s[l]):
                l += 1
            while r > l and not self.alpha_num(s[r]):
                r -= 1

            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1
        return True

    def alpha_num(self, c):
        return (
            ord("A") <= ord(c) <= ord("Z")
            or ord("a") <= ord(c) <= ord("z")
            or ord("0") <= ord(c) <= ord("9")
        )
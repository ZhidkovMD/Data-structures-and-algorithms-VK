from collections import deque


class Solution1:
    def is_subsequence(self, s: str, t: str) -> bool:
        i = 0
        len_s = len(s)
        len_t = len(t)

        for j in range(len_t):
            if i < len_s and s[i] == t[j]:
                i += 1

        return i == len_s


class Solution2:
    def is_subsequence(self, s: str, t: str) -> bool:
        queue = deque(s)

        for char in t:
            if queue and char == queue[0]:
                queue.popleft()

        return not queue


class Solution3:
    def is_subsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1

        return i == len(s)
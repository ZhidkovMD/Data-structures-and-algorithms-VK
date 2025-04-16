from collections import defaultdict
from typing import List


def group_anagrams(strs: List[str]) -> List[List[str]]:
    result = defaultdict(list)
    for string in strs:
        count = [0] * 26
        for char in string:
            count[ord(char) - ord("a")] += 1
        result[tuple(count)].append(string)
    return list(result.values())
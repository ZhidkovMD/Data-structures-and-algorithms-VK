def find_the_difference(s: str, t: str) -> str:
    count_s = {}
    count_t = {}
    
    for char in s:
        count_s[char] = 1 + count_s.get(char, 0)

    for char in t:
        count_t[char] = 1 + count_t.get(char, 0)

    for char in count_t:
        if char not in count_s:
            return char
        if count_s[char] < count_t[char]:
            return char
class Solution:
    def is_valid_parentheses(self, s: str, k: int) -> bool:
        n = len(s)
        if n == 0:
            return True
        
        if k >= n:
            return True
        
        balance = 0
        min_deletions = 0
        
        for char in s:
            if char == '(':
                balance += 1
            else:
                balance -= 1
            
            if balance < 0:
                min_deletions += 1
                balance = 0
        
        min_deletions += balance
        
        remaining_length = n - min_deletions
        if remaining_length % 2 != 0:
            min_deletions += 1
        
        return min_deletions <= k and (n - k) % 2 == 0
def count_binary_strings(n: int) -> int:
    if n == 0:
        return 0
    a = 1
    b = 1
    for _ in range(2, n + 1):
        new_a = a + b
        new_b = a
        a, b = new_a, new_b
    return a + b
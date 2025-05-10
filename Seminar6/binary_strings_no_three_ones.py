def count_binary_strings_no_three_ones(n: int) -> int:
    if n == 0:
        return 0
    
    a = 1
    b = 1
    c = 0
    for i in range(2, n + 1):
        new_a = a + b + c
        new_b = a
        new_c = b
        a, b, c = new_a, new_b, new_c
    return a + b + c
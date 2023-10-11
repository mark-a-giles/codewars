def count_bits(n):
    one_count = 0
    for char in bin(n):
        if (char == '1'):
            one_count = one_count + 1
    return one_count
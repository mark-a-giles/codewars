def move_zeros(lst):
    new_list = []
    zero_count = 0
    for i in lst:
        if i == 0:
            zero_count = zero_count + 1
        else:
            new_list.append(i)
    for i in range(zero_count):
        new_list.append(0)
    return new_list

result = move_zeros([1, 0, 1, 2, 0, 1, 3])
print(result)
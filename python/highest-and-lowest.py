def high_and_low(numbers):
    num_array = numbers.split()
    high = int(num_array[0])
    low = int(num_array[0])
    for value in numbers.split():
        if (high < int(value)):
            high = int(value)
        if (low > int(value)):
            low = int(value)
    return '{} {}'.format(high, low)
r = high_and_low("1 9 3 4 -5")
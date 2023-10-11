def is_valid_walk(walk):
    v = 0
    h = 0
    if (len(walk) != 10):
        return False
    for change in walk:
        if change == 'n':
            v = v + 1
        elif change == 's':
            v = v - 1
        elif change == 'e':
            h = h + 1
        elif change == 'w':
            h = h - 1
    if (v == 0 and h == 0):
        return True
    else:
        return False

result = is_valid_walk(['n','s','n','s','n','s','n','s','n','n'])
print(result)
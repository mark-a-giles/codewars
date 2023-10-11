def array_diff(a, b):
    for item in reversed(a):
        while(item in b and item in a):
            a.remove(item)
    return a
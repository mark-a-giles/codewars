def solution(s):
    string_pairs = []
    for i in range(0, len(s), 2):
        string_pairs.append(s[i:i + 2])    
    if len(string_pairs[len(string_pairs) - 1]) == 1:
        string_pairs[len(string_pairs) - 1] += '_'
    return string_pairs

r1 = solution('asdfadsf')
r2 = solution('asdfads')

print(r1, r2)
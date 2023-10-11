# Consider a sequence u where u is defined as follows:

# The number u(0) = 1 is the first one in u.
# For each x in u, then y = 2 * x + 1 and z = 3 * x + 1 must be in u too.
# There are no other numbers in u.
# Ex: u = [1, 3, 4, 7, 9, 10, 13, 15, 19, 21, 22, 27, ...]

# 1 gives 3 and 4, then 3 gives 7 and 10, 4 gives 9 and 13, then 7 gives 15 and 22 and so on...

# Task:
# Given parameter n the function dbl_linear (or dblLinear...) returns the element u(n) of the ordered (with <) sequence u (so, there are no duplicates).

# Example:
# dbl_linear(10) should return 22

# Note:
# Focus attention on efficiency
def dbl_linear(n):
    working_array = [1]
    for index in range(int(n)):
        y = 2 * working_array[index] + 1
        z = 3 * working_array[index] + 1
        if y not in working_array:
            working_array.append(y)
        if z not in working_array:
            working_array.append(z)
        working_array[n:len(working_array)].sort()
    working_array.sort()
    return working_array[n]

r = dbl_linear(30)
print(r)
# r2 = dbl_linear(64)
# print(r2)
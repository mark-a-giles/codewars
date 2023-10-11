def narcissistic(value):
    length = len(str(value))
    total = 0
    for position_value in str(value):
        total = total + int(position_value) ** length
    if value == total:
        return True
    else:
        return False

result = narcissistic(371)
print(result)
# narcissistic(371)
        # test.assert_equals(narcissistic(122), False, '122 is not narcissistic')
        # test.assert_equals(narcissistic(4887), False, '4887 is not narcissistic')
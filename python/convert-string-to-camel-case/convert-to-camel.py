
def to_camel_case(text):
    text = list(text)
    for idx, char in enumerate(text):
        if (char == '-' or char == '_'):
            text[idx] = ''
            text[idx + 1] = text[idx + 1].upper()
    return "".join(text)

camel_case = to_camel_case('the-stealth-warrior')
print(camel_case)
def spin_words(sentence):
    reversed_sentence = ""
    for idx, character in enumerate(sentence):
        reversed_sentence = character + reversed_sentence
    return reversed_sentence


spin_words('test')
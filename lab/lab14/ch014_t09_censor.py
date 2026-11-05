def censor(text, word):
    asterisks = '*' * len(word)
    result = text.replace(word, asterisks)
    return result


print(censor("this hackse is wack hack", "hack"))

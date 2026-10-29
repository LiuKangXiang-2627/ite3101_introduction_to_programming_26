def censor(text, word):
    asterisks = '*' * len(word)
    result = text.replace(word, stars)
    return result


print(censor("this hack is wack hack", "hack"))

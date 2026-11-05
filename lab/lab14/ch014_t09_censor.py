def censor(text, word):
    result = []
    for s in text.split():
        if s == word:
            result.append("*",len(word))

print(censor("this hack is wack hack", "hack"))
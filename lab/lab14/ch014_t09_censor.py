def censor(text, word):
    result = []
    for s in text.split():
        if s == word:
            result.append("*"*len(word))
        else:
            result.append(s)

print(censor("this hack is wack hack", "hack"))
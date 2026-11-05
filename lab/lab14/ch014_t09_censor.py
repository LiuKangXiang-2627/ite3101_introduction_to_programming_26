def censor(text, word):
    result = []
    for s in text.split():
        if s == word:
            result.append("*"*len(word))
        else:
            

print(censor("this hack is wack hack", "hack"))
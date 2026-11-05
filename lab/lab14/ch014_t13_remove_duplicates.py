def remove_duplicates(number):
    result=[]
    for i in number:
        if i not in number:
            result.append(i)
    return
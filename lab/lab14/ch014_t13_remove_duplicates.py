def remove_duplicates(number):
    result=[]
    for i in number:
        if i not in result:
            result.append(i)
    return result
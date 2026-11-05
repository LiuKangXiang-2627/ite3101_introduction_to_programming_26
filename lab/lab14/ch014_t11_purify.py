def purify(seq):
    result=[]
    for i in seq:
        if i %2 == 0:
            result.append(i)
    return result

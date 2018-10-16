def cap_join(string1):

    names=[]
    for index1 in string1:
        names.append(index1[0].upper() + index1[1:])
    return ' '.join(names)

string2 = ("calvin", "and", "hobbes", "are", "the", "first", "spacemen", "on","mars")

print(cap_join(string2))
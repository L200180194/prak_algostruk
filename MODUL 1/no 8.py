#apakah a terkandung dalam b
#no 10
def apakahTerkandung(a, b):
    x=0
    for i in range(len(b)):
        if a in b:
            x=True
        else :
            x=False
    return x

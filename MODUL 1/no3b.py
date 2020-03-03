print("NO 3b")
def jumlahhurufk(x):
    vowel =  ["A","I","U","E","O","a","i","u","e","o"]
    jv= 0
    jm = len(x)
    for char in x :
        if char not in vowel :
            jv +=1
    
    return (jm,jv)

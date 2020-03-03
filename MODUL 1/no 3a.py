print("NO 3a")
def jumlahhurufvokal(x):
    vowel =  ["A","I","U","E","O","a","i","u","e","o"]
    jv= 0
    jm = len(x)
    for char in x :
        if char in vowel :
            jv +=1
    
    return (jm,jv)
    
    

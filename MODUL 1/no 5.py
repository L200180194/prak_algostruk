from math import sqrt as sq
print('NO 5')
def apakahPrima(n):
    n=int(n)
    assert n>=0
    primaKecil =[2,3,5,7,11]
    bukanPrKecil= [0,1,4,6,8,9,10]
    if n in primaKecil :
        return true
    elif n in bukanPrKecil :
        return false
    else :
        for i in range (2,int(sq(n))+1):
            if n % i == 0:  # cek nilai jika n habis dibagi i sama dengan 0
                return False  # menampilkan False
            return True


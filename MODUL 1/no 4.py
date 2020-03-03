import math
print('NO 4')
def rerata(b) :
    hasil = 0
    for i in range(len(b)):
        hasil += b[i]
    hasil = hasil /len(b)
    return hasil
def variansi(n):
    hasil=0
    bag1=0
    bag2=0
    bag3= len(n)*(len(n)-1)
    for i in range(len(n)):
        bag1 += (n[i]*n[i])
        bag2 += n[i]
    hasil=((len(n)*bag1)-(bag2*bag2))/bag3
    return hasil

def stdev(n):
    hasil=0
    bag1=0
    bag2=0
    bag3= len(n)*(len(n)-1)
    for i in range(len(n)):
        bag1 += (n[i]*n[i])
        bag2 += n[i]
    hasil=math.sqrt(((len(n)*bag1)-(bag2*bag2))/bag3)
    return hasil



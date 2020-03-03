print ('NO 6')
bawah=2
atas=1000
if bawah>=1 and atas>1:
    for x in range(bawah,atas):
        prima=True
        for i in range(2,x):
            if(x%i==0):
                prima=False
        if prima==True:
            print(x)
else:
    print("Bukan Bilangan Prima")

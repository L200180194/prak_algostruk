#no 9
for i in range (1,101):
    if i % 3== 0 and i % 5 != 0:
        print ("python")
    elif i  %3 !=0 and i % 5== 0 :
        print ("UMS")
    elif i  %3 ==0 and i % 5== 0 :
        print (" Python UMS")
    else :
        print(i)

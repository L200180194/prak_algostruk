print("No 1---------------------------------------------------------------------------------------------------------------------------------------------------------")
#Nomor 1
import re
f=open('indonesia.txt','r', encoding='latin1')
teks = f.read()
f.close()
print(re.findall(r'me\w+',teks.lower()))
print("\n")

    
#Nomor 2
print("No 2---------------------------------------------------------------------------------------------------------------------------------------------------------")
import re
f=open('Indonesia.txt','r', encoding='latin1')
teks2 = f.read()
f.close()
print(re.findall(r"di\w+",teks2.lower()))
print("\n")
    
#Nomor 3
print("No 3---------------------------------------------------------------------------------------------------------------------------------------------------------")
import re
f=open('Indonesia.txt','r', encoding='latin1')
teks3 = f.read()
f.close()
print(re.findall(r"di \w+",teks3))
print("\n")

#Nomor 4a
print("No 4a---------------------------------------------------------------------------------------------------------------------------------------------------------")
import re
f=open('KEI.html','r', encoding='latin1')
teks4 = f.read()
f.close()
print(re.findall(r'([\w+]+)</a></td>',teks4))
print("\n")

#Nomor 4b
print("No 4b---------------------------------------------------------------------------------------------------------------------------------------------------------")
f=open('KEI.html','r', encoding='latin1')
teks4 = f.read()
f.close()
string=re.findall(r'title="([\w+]+)">',teks4)
string=re.findall(r'">([\w+]+)</a></td>\n<td>([0-9.]+)</td>',teks4)
a=[]
for i in string:
    a.append((i[0], float(i[1])))
print(a)


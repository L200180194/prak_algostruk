#NO 1,2, dan 3
class pesan(object):
    """sebuah class bernama pesan untuk memahami konsep class dan object"""
    def __init__(self, sebuahstring):
        self.teks=sebuahstring
    def cetakini(self):
        print(self.teks)
    def cetakpakaihurufkapital(self):
        print(str.upper(self.teks))
    def cetakpakaihurufkecil(self):
        print(str.lower(self.teks))
    def jumlahkar(self) :
        return len(self.teks)
    def cetakjumlahkarakter(self):
        print("kalimatku mempunyai ", len(self.teks),"karakter")
    def perbarui(self,stringbaru):
        self.teks= stringbaru
    def apakahTerkandung(self, b):
        if b in self.teks:
            return True
        else:
            return False
    def jumlahhurufk(self):
        vowel =  ["A","I","U","E","O","a","i","u","e","o"]
        jv= 0
        jm = len(self.teks)
        for char in self.teks :
            if char not in vowel :
                jv +=1
        print (jv)
    def jumlahhurufvokal(self):
        vowel =  ["A","I","U","E","O","a","i","u","e","o"]
        jv= 0
        jm = len(self.teks)
        for char in self.teks :
            if char in vowel :
                jv +=1
        print(jv)

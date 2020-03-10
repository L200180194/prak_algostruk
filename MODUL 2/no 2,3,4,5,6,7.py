#NO 2,3,4,5,6, dan7
from latihan23 import *
class mahasiswa(manusia) :
    """class mahasiswa yang dibangun dari class manusia """
    def __init__(self,) :
#NO 3
        """Metode inisiasi ini untuk menutup inisiasi di class manusia"""
        self.nama= input(" Masukkan Nama :")
        self.NIM=input("Masukkan NIM :")
        self.kotatinggal=input("Masukkan kota tinggal :")
        self.uangsaku=input(" Masukkan Uang saku : ")
    def __str__(self):
        s= self.nama+', NIM,' +str(self.NIM)\
           +'. Tinggal di' + self.kotatinggal\
           +'. uang saku Rp' + str(self.uangsaku)\
           +'tiap bulanya'
        return s
    def ambilnama(self):
        return self.nama
    def ambilNIM(self):
        return self.NIM
    def ambiluangsaku(self):
        return self.uangsaku
    def makan(self,s):
        """metode ini menutum metode 'makan' class manusia
            mahasiswa kalau makan sambil belajar"""
        print("saya baru saja makan",s,"sambil belajar")
        self.keadaan='kenyng'
#No 2
    def ambilkotatinggal(self):
        return self.kotatinggal
    def perbarui(self,kota):
        self.kotatinggal=kota
    def tambahuangsaku(self,b):
        self.uangsaku=int(self.uangsaku) + int(b)
        
#NO 4
    listkul=[]
    def listkuliah(self,):
        print (self.listkul)
    def ambilkuliah(self,matkul ):
        self.listkul.append(matkul)
#No 5
    def hapuskuliah(self,matkul ):
        self.listkul.remove(matkul)
#No 6

class siswaSMA(object):
    def __init__(self,nama,kelas,alamat):
        self.nama=nama
        self.alamat=alamat
        self.kelas=kelas
    def cetak (self):
        print("hi "+self.nama+" kamu berada dikelas : "+self.kelas)



#no 7
"""
NIM berasal dari class mahasiswa
ambilNIM berasal dari class mahasiswa
ambilNama berasal ddari class mahasiswa
ambilUangSaku berasal dari class mahasiswa
katakanPy berasal dari class MhsTIF
keadaan berasal dari class Manusia
kotaTinggal berasal dari class Mahasiswa
makan berasal dari class Manusia
mengalikanDenganDua berasal dari class Manusia
nama berasal dari class Mahasiswa dan Manusia
listKuliah berasal dari class Mahasiswa
ambilKuliah berasal dari class Mahasiswa
hapusKuliah berasal dari class Mahasiswa
tambahUangSaku berasal dari class Mahasiswa
uangSaku berasal dari class Mahasiswa
ambilKotaTinggal dari class Mahasiswa
olahraga berasal dari class Manusia
perbaruiKotaTinggal berasal dari class Mahasiswa
ucapkanSalam berasal dari class Manusia
"""


        

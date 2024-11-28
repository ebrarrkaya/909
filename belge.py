tr=int(input("Lutfen Turkce notunuzu giriniz: "))
mat=int(input("Lutfen Matematik notunuzu giriniz: "))
tar=int(input("Lutfen Tarih notunuzu giriniz: "))
ing=int(input("Lutfen İngilizce notunuzu giriniz: "))
fiz=int(input("Lutfen Fizik notunuzu giriniz: "))
ort=((tr*5)+(mat*6)+(tar*2)+(ing*4)+(fiz*4))/21
print("Ortalamaniz: {}".format(ort))
if ort>=85:
    print("Takdir belgesi almaya hak kazandiniz!")
elif 85>ort>70:
    print("Tesekkur belgesi almaya hak kazandiniz!")
else:
    print("Belge alamazsiniz.")

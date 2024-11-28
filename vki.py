boy=float(input("Lutfen boyunuzu giriniz: "))
kilo=float(input("Lutfen kilonuzu giriniz: "))
vki=kilo/(boy*boy)
if(vki<18.5):
    print("Zayifsiniz!")
elif(22.0<vki and vki<24.9):
    print("Sagliklisiniz!")
elif(25.0<vki and vki<29.0):
    print("Sismansiniz!")
elif(30.0<vki and vki<40.0):
    print("Obezsiniz!")
elif(vki>40.0):
    print("Morbid Obezsiniz!")

x=input("Celsius'un Fahrenheit donusumu icin f'ye, Fahrenheit'in Celsius'a donusumu icin c'ye basiniz: ")
if x=="f":
    ce=float(input("Fahrenheit'a cevrilecek Celsius degerini giriniz: "))
    print(ce*1.8+32)
elif x=="c":
    fa=float(input("Celsius'a cevrilecek Fahrenheit degerini giriniz: "))
    print((fa-32)/1.8)

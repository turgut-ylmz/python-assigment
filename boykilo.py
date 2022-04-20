kilo = float(input("kilonuzu giriniz:"))
boy = float(input("boyunuzu giriniz:"))
endeks = (kilo/ (boy/100)**2)
if(endeks<18):
    print("zayıf")
    print(endeks)
elif(endeks>18 and endeks<=25):
    print("normal")
    print(endeks)
elif(endeks>25 and endeks<=30):
    print("obez")
    print(endeks)
else:
    print("ciddi obez")
    print(endeks)

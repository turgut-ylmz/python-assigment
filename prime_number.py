n = int(input("Lütfen sayı giriniz : "))

sayac = 0

for i in range(2,n):   

    if n%i==0 :

        sayac +=1

        break



if sayac == 0:

    print("asal sayı")

elif sayac != 0:

    print("asal değil")

print("""
*******************
ATM YE HOŞGELDİNİZ.
Lütefen yapmak sitediğiniz işlemi seçiniz.
1. Bakiye sorgulama
2. Para çekme
3. Para yatırma
Çıkmak için q ya basınız.
*******************
"""
)

bakiye=1000

while True:
    işlem=input("Yapmak istediğiniz işlemi seçiniz:")
    if işlem == "q" :
        print("güle güle")
        break
    elif işlem=="1":
        print("bakiyeniz {} tl dir.".format(bakiye))
    elif işlem == "2" :
        miktar=int(input("miktarı yazınız."))
        bakiye -=miktar
        if (bakiye - miktar < 0 ):
            print("bakiyeniz yetersiz.")
            continue
    elif işlem =="3":
        miktar=int(input("miktarı yazınız."))
        bakiye +=miktar
    else:
        print("geçersiz işlem.")

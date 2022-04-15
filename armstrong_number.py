a = int(input("sayı : "))

b = 0

c = a



while c > 0:

    d = c % 10

    b += d*d*d

    c //= 10

    if a == b:

        print(a, "bir Armstrong numarasıdır")

    else:

        print(a, "bir Armstrong numarası değil")

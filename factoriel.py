def FirstFactorial(num):
    fak = 1
    if num == 0 or num == 1 :
        return 1
    else:
        for i in range(2,num+1):
            fak *= i
        return fak
    return num
print(FirstFactorial(int(input())))

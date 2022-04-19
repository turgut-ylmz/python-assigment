n = int(input("number : "))
tau_list = []
counter = 0

for i in range(1,n+1):
    if n%i == 0 :
        counter +=1
        tau_list.append(i)
if n%counter == 0 :
    print("tau")
    print(tau_list)
    print(counter)
else:       
    print("not tau")
    print(tau_list)
    print(counter)

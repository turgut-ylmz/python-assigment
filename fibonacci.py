x = 1

y = 0

my_list = []

for i in range(10):

    z = x

    x = x + y

    y = z

    my_list.append(y)

print(my_list)

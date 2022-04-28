num = [1,2,3]
num_set = {1,2,3}
solution = [[]]
for index in range(len(num)) :
    
    solution = [i+[j] for i in solution for j in num_set.difference(set(i))]
    print(solution)

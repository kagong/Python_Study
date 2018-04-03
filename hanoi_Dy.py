n = int(input())
hanoi_list = [1]

for i in range(1,n):
    hanoi_list.append(2*hanoi_list[i-1]+1)

print (hanoi_list[n-1])

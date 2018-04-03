n =int(input('n 을 입력하세요 :'))
k =int(input('k 을 입력하세요 :'))

list = []
for i in range(0,n+1):
    list.append([0]*(i+1))
    for j in range(0,i+1):
        if i == j:
            list[i][j] = 1
        elif j == 0 :
            list[i][j] = 1
        else:
            list[i][j] = list[i-1][j-1] + list [i-1][j]
result = list[n][k]

print ("Bin( %d, %d )는 %d 입니다." %( n, k, result))

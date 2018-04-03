"""i = int(input("가로 길이는? :"))
j = int(input("세로 길이는? :"))
L = [[1]*i]*j
num = 0
for i in L:
    for j in range(0,len(i)):
        i[j] = num
        num+=1
    print (i)
"""
"""
str = input()
tup = tuple(str.split())
print(tup)
"""
"""
dic = { 'a':123,'so':'good',1:2}
for i in dic.items():
    print(i)
a = '1'
b = '2'
c =tuple(a)
c+=tuple(b)
"""
"""
def hanoi(N, src, tmp, dest):
    if not isinstance(N, int):
        raise TypeError
    if N == 1:
        print("%d %d" %(src, dest))
        return 1
    else:
        cnt = hanoi(N-1, src, dest, tmp)
        print("%d %d" %(src, dest))
        cnt += hanoi(N-1, tmp, src, dest)

        cnt += 1

    return cnt

def hanoi_cnt(N):
    if not isinstance(N, int):
        raise TypeError
    if N == 1:
        return 1
    else:
        return hanoi_cnt(N-1) * 2 + 1

num = input()

print(hanoi_cnt(int(num)))
hanoi(int(num), 1, 2, 3)
"""
for i in range(10,0,-1):
    print(i)














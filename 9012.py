T = int(input())
for i in range(T):
    size = 0
    string =input()
    for ch in string:
        if ch == '(' :
            size +=1
        elif size == 0 :
            size = -1
            break
        else:
            size-=1
    if size == 0 :
        print('YES')
    else:
        print('NO')
            

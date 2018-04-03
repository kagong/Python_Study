size = int(input())
seq = input().split()
T = int(input())
result = {}
for i in range(1,size+1):
    result.update({(i,i):True})
for intval in range(1,size):
    for start in range(1,size+1):
        if start+intval > size:
            break
        elif seq[start-1] == seq [start + intval -1]:
            prev = result[(start+1,start+intval-1)]
            result.update({(start,start+intval):prev})
        else:
            result.update({(start,start+intval):False})
for i in range(T):
    S ,E = (int(x) for x in input().split())
    if result[(S,E)] is True:
        print("1")
    else :
        print("0")


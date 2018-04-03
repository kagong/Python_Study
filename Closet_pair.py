def dist( corr_1,corr_2):
    return (corr_2[0]-corr_1[0])**2+(corr_2[1]-corr_1[1])**2
def closest_pair(corr,n):
    if n > 3:
        mid = n//2 
        dl = int(closest_pair(corr[:mid] , mid))
        dr = int(closest_pair(corr[mid:] , n-mid))
        d = min(dl,dr)
        list = []
        for i in corr:
            if abs(i[0] - corr[mid][0]) < d**0.5:
                list.append((i[1],i[0]))
        list.sort()
        list_2=list.copy()
        for i in list:
            list_2.remove(i)
            for j in list_2:
                if abs(i[0] - j[0]) < d**0.5 :
                    temp = dist(i,j)
                    if temp < d:
                        d = temp
    elif n == 3:
        d = min(dist(corr[0],corr[1]),dist(corr[0],corr[2]),dist(corr[1],corr[2]))
    elif n == 2 :
        d = dist(corr[0],corr[1])
    else:
        d = 0
    return d
n = int(input())
corr = []
for i in range(0,n):
    x = input()
    corr += x.split()
    corr.insert(-1,(int(corr.pop(-2)),int(corr.pop())))
corr.sort()
d = closest_pair(corr,len(corr))
print(d)

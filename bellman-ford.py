v =int(input()) #total v
dist =[0]*v
#max = sys.maxint
e =int(input()) #total e
E=[[0]*v]
for i in range(e):
    E.append(tuple(int(x) for x in input().split()))
s =int(input()) #source
d = int(input()) #destination

for i in range(v):
    for (u,v,w) in E:
        if dist[u]+w < dist[v]:
            dist[v] = dist[u]+w
print(dist[d])


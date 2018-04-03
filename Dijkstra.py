import math
distMax= math.inf
class HEAP:
    def __init__(self,V,dist):
        self.heaptree=[V]+[x for x in range(V)]
        for i in range(V//2,0,-1):
            self.down(i)
    def dec(self,target):
        idx=self.heaptree[1:].index(target)+1
        while idx//2 > 0:
            if dist[self.heaptree[idx]] < dist[self.heaptree[idx//2]] :
                self.heaptree[idx] , self.heaptree[idx//2] =self.heaptree[idx//2] , self.heaptree[idx]
                idx//=2
            else:
                break
    def down(self,target):
        idx = child = target
        while child*2 <= self.heaptree[0] :
            child*=2
            if child+1 <= self.heaptree[0] and dist[self.heaptree[child+1]] <dist[self.heaptree[child]] :
                child+=1
            if  dist[self.heaptree[child]]<dist[self.heaptree[idx]] :
                self.heaptree[idx] , self.heaptree[child] =self.heaptree[child] , self.heaptree[idx]
                idx=child
            else:
                break
    def Del(self):
        if self.heaptree[0] < 1:
            print("error 입니다!")
            return -1
        elif self.heaptree[0] == 1:
            self.heaptree[0]=0
            return self.heaptree.pop()
        result=self.heaptree[1]
        self.heaptree[1]=self.heaptree.pop()
        self.heaptree[0]-=1
        self.down(1)
        return result
def dijkstra(dest):
    while True:
        u=heap.Del()
        if u == dest :
            break
        for (v,w) in adj[u]:
            if dist[u]+w<dist[v]:
                dist[v] = dist[u]+w
                heap.dec(v)
                path[v]=u
def printPath(v):
    if v != s:
        printPath(path[v])
    print(v,end=' ')
V = int(input("정점의 갯수를 입력해 주세영: "))
E = int(input("간선의 갯수를 입력해 주세영: "))
adj=[]
dist=[distMax]*V
for i in range(V):
    adj.append([])
print("간선의 정보를 %d번 입력해 주세영(u,v,w)"%E)
for i in range(E):
    u,v,w=(int(x) for x in input().split())
    adj[u].append((v,w))
    adj[v].append((u,w))
s,d=(int(x) for x in input("출발지와 도착지를 입력해 주세용:").split())
for (v,w) in adj[s]:
    dist[v]=w
dist[s]=0
heap=HEAP(V,dist)
heap.Del()
path=[0]*V
dijkstra(d)
print("거리는!",dist[d])
printPath(d)

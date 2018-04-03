V,E,src = (int(x) for x in input().split())
adj =[[] for i in range(V+1)]
for i in range(E):
    u,v = (int(x) for x in input().split())
    adj[u].append(v)
    adj[v].append(u)
stack = []
visit = [0*(V+1)]
while True:
    if stack[0] == src:
        print(stack.pop())
        break
    else:
        tar=stack.pop(0)
        for i in adj[tar]:
            
        

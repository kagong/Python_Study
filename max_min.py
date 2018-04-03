n = int(input())
k = int(input())
seq = [ int(x) for x in input().split() ]
seq.sort()
result = seq[k-1] - seq[0]
for i in range(1,len(seq)-k):
    if seq[i+k-1] - seq[i] < result:
        result = seq[i+k-1] - seq[i]
print (result)
    


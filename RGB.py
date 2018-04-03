n=int(input())
result = {'red':0,'green':0,'blue':0}
for i in range(n):
    in_list = input().split()
    R,G,B=(int(x) for x in in_list)
    r=min(G+result['green'],B+result['blue'])
    g=min(R+result['red'],B+result['blue'])
    b=min(R+result['red'],G+result['green'])
    result['red'],result['green'],result['blue']=r,g,b
print(min(result['red'],result['green'],result['blue']))
    

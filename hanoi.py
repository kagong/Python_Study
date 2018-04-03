list = []
def hanoi(ffrom,tto,num):
    if num >0:
        temp = 6 - ffrom - tto
        hanoi(ffrom,temp,num-1)
        list.append("%d, %d"%(ffrom,tto))
        hanoi(temp , tto, num-1)
num = int(input())
hanoi(1,3,num)
print (len(list))
for i in list:
    print (i)

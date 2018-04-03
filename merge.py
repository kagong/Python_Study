def merge(L):
    size=len(L)
    if size >= 2:
        left = L[:size//2]
        right = L[size//2:]
        left = merge(left)
        right = merge(right)
        Result = []
        for i in range(0,len(L)) :
            if len(left)  == 0:
                Result = Result + right
                break
            elif len(right) == 0:
                Result = Result + left
                break
            elif left[0] < right[0]:
                a = left.pop(0)
                Result.append(a)
            else:
                a = right.pop(0)
                Result.append(a)
        L = Result
    return L
a=[27,10,12,20,25,13,15,22]
a=merge(a)
print (a)

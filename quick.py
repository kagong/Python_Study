def quick(L):
    size=len(L)
    if size >= 2:
        left = []
        right = []
        pivot = L.pop(0)
        for i in L:
            if i < pivot :
                left.append(i)
            else :
                right.append(i)
        left = quick(left)
        right = quick(right)
        L=left
        L.append(pivot)
        L+=right
    return L
a = [12,12,41,15,2,1]
a = quick(a)
print (a)

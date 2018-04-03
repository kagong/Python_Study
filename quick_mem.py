
def quick(L):
    size=len(L)
    if size >= 2:
        pivot = L.pop(0)
        mid = 0
        for i in range(0,size-1):
            item = L.pop()
            if item < pivot:
                L.insert(0,item)
                mid += 1
            else:
                L.insert(mid,item)
        L.insert(mid,pivot)
        L[ : mid ] = quick(L[ : mid ])
        L[mid + 1 : ] = quick(L[mid + 1 : ])
    return L

a = [12,232,4,2,23,23,23,21,214,15,126,246,345,435,37,8,769,2,456,45,1]
a = quick(a)
print(a)

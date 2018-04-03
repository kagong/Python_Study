dic = {}
class Tree:
    freq = 1
    def __init__(self, ch=None, left=None, right=None):
        if ch != None:
            self.ch = str(ch)
        self.left  = left
        self.right = right
    def inc(self):
        self.freq=self.freq+1
    def huffcode(self,string):
        if self.left==self.right == None:
            dic[self.ch] = string
        else:
            self.left.huffcode(str(string+'0'))
            self.right.huffcode(str(string+'1'))
def Qsort(L):
    size =len(L)
    if(size > 1 ):
        pivot = L[0]
        j = 0
        for i in range(1,size):
            if L[i].freq < pivot.freq:
                j+=1
                L[i],L[j]=L[j],L[i]
        L[0],L[j]=L[j],L[0]
        return Qsort(L[:j])+[L[j]]+Qsort(L[j+1:])
    return L
def makeTree(L):
    for i in range(len(L)-1):
        leftNode = L.pop(0)
        rightNode=L.pop(0)
        result=leftNode.freq+rightNode.freq
        idx = -1
        for j in range(len(L)):
            if result<L[j].freq:
                idx = j
                break
        if idx == -1:
            L.append(Tree('',leftNode,rightNode))
        else:
            L.insert(idx,Tree('',leftNode,rightNode))
    return L[0]
string = input()
for ch in string:
    if ch in dic :
        dic[ch].inc()
    else:
        dic[ch]=Tree(ch)
Treelist = list(dic.values()).copy()
dic.clear()
Treelist=Qsort(Treelist)
root = makeTree(Treelist)
root.huffcode('')
if root.ch!='':
    dic[root.ch]='0'
print(dic)
for ch in string:
    print(dic[ch],end='')
    

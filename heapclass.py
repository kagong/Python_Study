class min_heap:
    def __init__(self,itemtype):
        self.data = []
        self.type=itemtype
    def input(self,itemlist):
        assert isinstance(itemlist, list)
        self.data = itemlist.copy()
        self.data.insert(0,None)
        self.heapify()
    def bubbledown(self,idx):#idx is index of target
        child = idx*2
        MAX = len(self.data)-1
        while child <= MAX:
            if child + 1 <= MAX and self.data[child] > self.data[child+1] :
                child +=1
            if self.data[idx] < self.data[child] :
                break
            else:
                self.data[idx] , self.data[child] = self.data[child] , self.data[idx]
                idx ,child = child,child*2                
    def bubbleup(self,idx):
        parent = idx // 2
        MAX = len(self.data)-1
        while parent != 0:
            if self.data[idx] < self.data[parent]:
                self.data[idx] , self.data[parent] = self.data[parent] , self.data[idx]
                idx ,parent = parent,parent//2
            else:
                break
    def heapify(self):
        MAX = len(self.data)-1
        for i in range(MAX//2,0,-1):
            self.bubbledown(i)
    def insaert(self,item):
        assert isinstance(item, self.type)
        MAX = len(self.data)-1
        self.data.append(item)
        MAX+=1
        self.bubbleup(MAX)
    def pop(self):
        MAX = len(self.data)-1
        if MAX == 0:
            return False
        else:
            self.data[0],self.data[1]=self.data[1],self.data[MAX]
            self.data.pop()
            self.bubbledown(1)
            return self.data[0]
    def heapsort(self):
        temp = self.pop()
        while temp is not False:
            print (temp,end = ' ')
            temp = self.pop()


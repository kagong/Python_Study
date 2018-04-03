class DEQUE:
    size = 0
    arr=[]
    def push_front(self,ch):
        self.arr.insert(0,int(ch))
        self.size+=1
    def push_back(self,ch):
        self.arr.append(int(ch))
        self.size+=1
    def pop_front(self):
        if self.size == 0:
            return -1
        else:
            self.size-=1
            return self.arr.pop(0)
    def pop_back(self):
        if self.size == 0:
            return -1
        else:
            self.size-=1
            return self.arr.pop()
    def front(self):
        if self.size == 0:
            return -1
        else:
            return self.arr[0]
    def back(self):
        if self.size == 0:
            return -1
        else:
            return self.arr[-1]
    def empty(self):
        if self.size == 0:
            return 1
        else:
            return 0
    def top(self):
        if self.size ==0:
            return -1
        else :
            return self.arr[-1]
n=int(input())
stack =DEQUE()
for i in range(n):
    command = input().split()
    if command[0] == 'push_front' :
        stack.push_front(command[1])
    elif command[0] == 'push_back' :
        stack.push_back(command[1])
    elif command[0] == 'pop_front' :
        print(stack.pop_front())
    elif command[0] == 'pop_back' :
        print(stack.pop_back())
    elif command[0] == 'size' :
        print(stack.size)
    elif command[0] == 'empty' :
        print(stack.empty())
    elif command[0] == 'front' :
        print(stack.front())
    elif command[0] == 'back' :
        print(stack.back())

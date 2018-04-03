class STACK:
    size = 0
    arr=[]
    def push(self,ch):
        self.arr.append(int(ch))
        self.size+=1
    def pop(self):
        if self.size == 0:
            return -1
        else:
            self.size -=1
            return self.arr.pop()
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
stack =STACK()
for i in range(n):
    command = input().split()
    if command[0] == 'push' :
        stack.push(command[1])
    elif command[0] == 'pop' :
        print(stack.pop())
    elif command[0] == 'size' :
        print(stack.size)
    elif command[0] == 'empty' :
        print(stack.empty())
    elif command[0] == 'top' :
        print(stack.top())

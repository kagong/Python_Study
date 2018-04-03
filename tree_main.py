from mytree import TreeNode
root = TreeNode(input())
treelist = [root]
childlist = []
while True:
    flag = True
    string = input()
    for item in string.split():
        temp = None
        if item is not '-':
            flag = False
            temp = TreeNode(item)
        childlist.append(temp)
    if flag is True:
        break
    else:
        idx = 0
        for node in treelist:
            if node is not None:
                node+(childlist[idx],childlist[idx+1])
            idx+=2
    treelist.clear()
    treelist = childlist.copy()
    childlist.clear()        

        
    
        

import bst
BSTlist = []
select = None
while True :
    print("--------메뉴--------")
    print("list : 트리 list 출력 ")
    print("select : 트리 선택")
    print("make : 트리 생성")
    print("exit : 종료")
    print("---------------------")
    command = input("선택 : ")
    if command == 'list':
        for i in BSTlist:
            print("root is ",i.item)
    elif command == 'make':
        num = int(input("root의 값 : "))
        BSTlist.append(bst.BSTnode(num))
    elif command == 'select':
        select = int(input("트리 선택 : "))
        print("1 : 트리 노드 삽입")
        print("2 : 트리 노드 삭제")
        print("3 : 트리 병합")
        print("4 : 트리 preorder")
        print("5 : 트리 inorder")
        print("6 : 트리 postorder")
        mode = int(input("모드를 선택해 주세용! "))
        if mode == 1:
            BSTlist[select].ins(int(input('추가할 값 : ')))
        elif mode == 2:
            if BSTlist[select].delete(int(input('삭제할 값 : '))) is False:
                print("삭제 실패!")
            else :
                print("삭제 성공!")
            if BSTlist[select].item == None:
                BSTlist.pop(select)
        elif mode == 3:
            second = int(input("병합할 트리를 선택해 주세요 : "))
            root = bst.BSTnode(0)
            root.left , root.right = BSTlist[select] , BSTlist[second]
            if root.merge() is False:
                print("병합 실패!")
            else:
                if select < second :
                    BSTlist.pop(second)
                    BSTlist.pop(select)
                else:
                    BSTlist.pop(select)
                    BSTlist.pop(second)
                BSTlist.insert(0,root)
        elif mode == 4:
            BSTlist[select].preorder()
        elif mode == 5:
            BSTlist[select].inorder()
        elif mode == 6:
            BSTlist[select].postorder()
    else :
        break;

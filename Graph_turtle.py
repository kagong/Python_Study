from turtle import *
speed(0)
R = 40
Cirlist=[]
arr=[]
def Setpen(x,y):
    up()
    goto(x,y)
    down()
def calculateCor(From,To):
    x1,y1=From
    x2,y2=To
    intval_X=x1-x2
    intval_Y=y1-y2
    d = (abs(intval_X)**2+abs(intval_Y)**2)**(0.5)
    y=y1+-1*R*intval_Y/d
    x=x1+-1*R*intval_X/d
    return(x,y)
def drawEdge(From,To):
    st()
    start= calculateCor(From,To)
    end= calculateCor(To,From)
    Setpen(start[0],start[1])
    goto(end)
    ht()
def drawbox(x,y):
    Setpen(x,y)
    goto(x+100,y)
    goto(x+100,y-50)
    goto(x,y-50)
    goto(x,y)
def drawinit():
    drawbox(-700,350)
    Setpen(-650,320)
    write("V mode")
    drawbox(-700,250)
    Setpen(-650,220)
    write("E mode")
    drawbox(-700,150)
    Setpen(-650,120)
    write("DFS mode")
    drawbox(-700,50)
    Setpen(-650,20)
    write("BFS mode")
    drawbox(-700,-50)
    Setpen(-650,-80)
    write("Quit")
    ht()
    for u in Cirlist:
        u.drawCir()
        """
        for v in u.adj:
            drawEdge(u.cor,v.cor)
        """
class Cir:
    def __init__(self,x,y):
        self.color='white'
        self.cor =(x,y)
        self.adj=[]
    def __sub__(self,other):
        self.adj.append(other)
        other.adj.append(self)
        drawEdge(self.cor,other.cor)
    def drawCir(self):
        st()
        Setpen(self.cor[0],self.cor[1]-R)
        color('black',self.color)
        begin_fill()
        circle(R)
        end_fill()
        ht()
    def DFS(self):
        
        arr.append(self)
        while len(arr) != 0 :
            u=arr.pop(0)
            if u.color == 'blue' :
                continue
            u.color='blue'
            speed(6)
            u.drawCir()
            speed(0)
            for v in u.adj:
                if v.color == 'white':
                    arr.insert(0,v)
    def BFS(self):
        arr.append(self)
        while len(arr) != 0 :
            u=arr.pop(0)
            if u.color == 'blue' :
                continue
            u.color='blue'
            speed(6)
            u.drawCir()
            speed(0)
            for v in u.adj:
                if v.color == 'white':
                    arr.append(v)
def boxcheck(boxX,boxY,x,y):
    if x<boxX or boxX+100<x:
        return False
    elif y<boxY-50 or boxY<y:
        return False
    else:
        return True
def circheck(x,y):
    temp = None
    for i in Cirlist:
            ix,iy=i.cor
            d = (abs(ix-x)**2+abs(iy-y)**2)**(1/2)
            if d <= R:
                temp = i
                break
    return temp
def action(x,y):
    global mode,U,V
    if boxcheck(-700,350,x,y) == True:
        for i in Cirlist:
            i.color='white'
        drawinit()
        mode = "V"
    elif boxcheck(-700,250,x,y) == True:
        for i in Cirlist:
            i.color='white'
        drawinit()
        mode = "E_u"
    elif boxcheck(-700,150,x,y) == True:
        for i in Cirlist:
            i.color='white'
        drawinit()
        mode = "DFS"
    elif boxcheck(-700,50,x,y) == True:
        for i in Cirlist:
            i.color='white'
        drawinit()
        mode = "BFS"
    elif boxcheck(-700,-50,x,y) == True:
        mode = "QUIT"
    elif mode == "V" :
        if circheck(x,y) == None :
            CirNode = Cir(x,y)
            CirNode.drawCir()
            Cirlist.append(CirNode)
        else :
            print("이상함")
    elif mode == "E_u" :
        U = circheck(x,y) 
        if U != None:
            U.color='blue'
            U.drawCir()
            mode = "E_v"
    elif mode == "E_v" :
        V = circheck(x,y)
        if V != None and V != U :
            U-V
            U.color='white'
            U.drawCir()
            mode = "E_u"
    elif mode == "DFS" :
        V = circheck(x,y)
        if V != None:
            V.DFS()
    elif mode == "BFS" :
        V = circheck(x,y)
        if V != None:
            V.BFS()

drawinit()
while True:
    onscreenclick(action)
    if mode == "QUIT" :
        break
    onclick(None)
bye()

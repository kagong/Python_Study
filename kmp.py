def prefix(pat):
    List = [-1]
    for i in range(1,len(pat)):
        if pat[List[i-1]+1] == pat[i] :
            List.append(List[i-1]+1)
        else:
            List.append(-1)
    return List
def kmp(text,pat):
    prefixlist = prefix(pat)
    #print(prefixlist)
    idx,start,i = 0,0,0
    result = []
    for i in range(len(text)):
        if text[i] == pat[idx]:
            idx += 1
        else:
            while True:
                if idx == 0 :
                    break
                idx = prefixlist[idx-1] + 1
                if text[i] == pat[idx]:
                    idx+=1
                    break
                if idx == prefixlist[idx-1] +1 :
                    break
            start = i - idx + 1
        if idx > len(pat) - 1 :
            result.append(start)
            start = i - prefixlist[-1] 
            idx = prefixlist[-1] + 1
    return result
text = input("텍스트를 입력해 주세용! : ")
pat = input("패턴을 입력해 주세용! : ")
for idx in kmp(text,pat):
    print(text[idx:])
    

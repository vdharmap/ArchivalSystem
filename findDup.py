#/usr/local/bin/python3
# _*_ coding : utf-8 _*_

import numpy as np
#duplicate


def pointerDup(lst):
    dlst=[]
    for p1 in range(len(lst)):
       # print("Pointer:",lst[p1])
        p2=0
        while p2 < len(lst):
            if p1!=p2 and lst[p1] == lst [p2]:
                #break
                #print(lst[p1])
                if lst[p1] not in dlst:
                    dlst.append(lst[p1]) 
            p2+=1 
    return dlst

def findDup(lst):
    slst = np.sort(np.array(lst))
    print(slst)
    rlst=[];
    tmp=0
    dlst=[];
    for n in slst:
            if [n==tmp]:
                if n not in rlst:
                    rlst.append(n)  
                else: 
                    if n not in dlst:
                       dlst.append(n)
            tmp=n
    return dlst

def setDup(lst):
   sdlst = list(set(lst))
   return sdlst

def comDup(lst):
    res = []
    [res.append(x) for x in lst if x not in res]
    return res

#main
def main():
    lst = [2,4,2,4,5,6,3,3,5,23,42,3,4,3,34,5,2,4,5,5,6,6,7,7,34]
    plst = pointerDup(lst)
    print("Pointer SOL:",str(plst)) 
    #dlst=findDup(lst)
    #sdlst=setDup(lst)
    #rlst=comDup(lst)
    #print("SET SOL:",str(sdlst))
    #print("TMP SOL:",str(dlst))
    #print("COMP SOL:",str(rlst))

if __name__ == "__main__":
    main()
    


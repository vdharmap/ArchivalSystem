# list 
from functools import reduce

def maxLambda(list):
     list.sort(key=lambda x: x[2])
     print (list[-1][2])
    
def maxValue(lst):
    tlst=[]
    maxVal=0
    for i in lst:
        if i[2] > maxVal:
            maxVal=i[2]
       # tlst.append(i[2])
    print(maxVal)
   # tlst.sort()
    #print(tlst[len(tlst)-1])
def avgValue(lst):
    num=0
    for i in (lst):
        #print(i[2])
        num = num + i[2]
    avgVal = num/len(lst)
    print(avgVal)
def nthelem(list):
    print((lambda x:x[2]))


def main():
    lst = [[123,"abc",10],[124,"dbg",5],[145,"245",50],[180,"a123",15]]
    maxValue(lst)
    avgValue(lst)
    maxLambda(lst)
    #print ((lambda x,y,z:x+y+z)(1,1,2))
    #numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    #print (sorted(numbers,key=lambda x:-x))
    nthelem(lst)
    print(reduce(lambda x,y:x+y,list)(list))

if __name__ == "__main__": 
    main()

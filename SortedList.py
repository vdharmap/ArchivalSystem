#/usr/local/bin/python3
# _*_ coding: utf-8 _*_
import numpy as np
#MergeList

def mergeList(lis1,lis2):
    print(np.sort(np.array(lis1+lis2)))
    

#main    
lis1 = [2,8,9]
lis2 = [1,5,6,7]
mergeList(lis1,lis2)
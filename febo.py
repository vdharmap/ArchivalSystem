#!/usr/local/bin/python3
#_*_ coding: utf-8 _*_
# add code for fibonacci's - 0,1,1,2,3,5,8,13




def fadd(i):
    if i==0:
       return 0
    elif(i==1):
        return 1
    else:
        return fadd(i-2) + fadd(i-1)


def main():
    index=int(input("Index Value:="))
    for i in range(0, index):
        print(fadd(i))

if ( __name__) == "__main__":
    main()
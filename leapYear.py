#/usr/local/bin/python3
#_*_ coding: utf-8 _*_ 

def chk(tyear):
    if (tyear/4 == 0 and tyear/100 != 0 and tyear/400 != 0):
        print ("Leap Year",tyear)
    else:
        print ("Not Leap Year",tyear)

def getinput():
    tyear = int(input("Enter Year(YYYY?:"))
    if len(str(tyear)) != 4:
        getinput() 
    else:
        return tyear

def main():
    tyear = getinput()
    chk(tyear)
if __name__ == "__main__":
    main()
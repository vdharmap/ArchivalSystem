#/usr/local/bin/python3
#_*_ coding: utf-8 _*_

#another mehtod to swap the values is to mathematically swap the values
# x=x+y
# y=x-y
# x=x-y
#this will swap the values of x and y

def swap(x,y):
    x,y=y,x
    return x,y

def get_input():
    x=int(input("Enter the value of x:"))
    y=int(input("Enter the value of y:"))
    return x,y

def main():
    x,y=get_input()
    print("Before Swap:",x,y)
    x,y=swap(x,y)
    print("After Swap:",x,y)
if __name__ == "__main__":
    main()
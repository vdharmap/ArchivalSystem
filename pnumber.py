#!/usr/local/bin/python3
#_*_ coding: utf-8 _*_


def sign(n):
    if ( n>=0):
        print("positive")
    else:
        print("negetive")

def main():
    n = float(input("Number?:"))
    sign(n)


if __name__ == "__main__":
    main()
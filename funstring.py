#!/usr/local/bin/python3
#_*_ coding = utf-8 _*_

def rev(mstring):
    rstring = ""
    for i in mstring:
        rstring = i + rstring
    return rstring

def main():
    mstring = str(input("Enter string:"))
    print (rev(mstring))


if __name__ == "__main__":
    main()
#!/usr/bin/env python2
# -.- coding: utf-8 -.-
def main():
    a1,b1= map(int, raw_input().strip().split(" "))
    a2,b2= map(int, raw_input().strip().split(" "))
    a3,b3= map(int, raw_input().strip().split(" "))
    for i in (a2,b2,a3,b3):
        if i > max((a1,b1)):
            print("NO")
            return
    options = ((a2+a3, b2+b3), (a2+b3, b2+a3),
            (b2+a3, a2+b3), (b2+b3,a2+a3))
    for xsum,ysum in options:
        if xsum <= a1 and ysum <=b1:
            print("YES")
            return
    if a2 < a1:
        if ((a1-a2) >= a3 and b1 >= b3) or\
                ((a1-a2) >= b3 and b1 >= a3):
            print("YES")
            return
    if a2 < b1:
        if ((b1-a2) >= a3 and a1 >= b3) or\
                ((b1-a2) >= b3 and a1 >= a3):
            print("YES")
            return
    print("NO")


if __name__ == "__main__":
    main()

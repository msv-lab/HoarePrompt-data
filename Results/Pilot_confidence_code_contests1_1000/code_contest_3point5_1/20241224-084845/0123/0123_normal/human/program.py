#!/usr/bin/python

import sys

def main(argv):
    line = sys.stdin.readline()
    while line:
        N = int(line)
        P = map(lambda x: int(x), sys.stdin.readline().split(" "))

        counter = 0
        for i in xrange(len(P)):
            index = i + 1
            if P[i] == index:
                if i > 0:
                    if P[i - 1] == index - 1:
                        P[i] = P[i - 1]
                    elif P[i + 1] == index + 1:
                        P[i], P[i + 1] = P[i + 1], P[i]
                    else:
                        P[i] = P[i - 1]
                else:
                    P[i], P[i + 1] = P[i + 1], P[i]
                counter += 1
        print(counter)
        
        line = sys.stdin.readline()

if __name__ == "__main__":
    main(sys.argv)
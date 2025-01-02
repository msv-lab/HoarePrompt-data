from collections import defaultdict
from functools import reduce
from bisect import bisect_right
from bisect import bisect_left
import copy
import atexit, io, sys
def main():
    buffer = io.BytesIO() 
    sys.stdout = buffer

    @atexit.register 
    def write(): 
        sys.__stdout__.write(buffer.getvalue())
    for _ in xrange(input()):
        n=input()
        l=raw_input()
        l+='+'
        c1=0
        c0=0
        OI=0
        IO=0
        for i in xrange(1,n):
            if l[i]=='1' and l[i-1]=='1' :
                c1+=1
            if l[i]=='0' and l[i-1]=='0' :
                c0+=1
            if l[i]=='1' and l[i-1]=='0' and l[i+1]!='0':
                OI+=1
            if l[i]=='0' and l[i-1]=='1' and l[i+1]!='1':
                IO+=1
        #print n,OI,IO,c1,c0
        print(min(OI,IO)+min(c1,c0))
                
            

if __name__ == '__main__':
    main()
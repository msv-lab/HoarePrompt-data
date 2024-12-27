# python2
import sys, threading, os.path
import collections, heapq, math,bisect

sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)

def main():
    if os.path.exists('input.txt'):
        input = open('input.txt', 'r')
    else:
        input = sys.stdin
    #--------------------------------INPUT---------------------------------
    k = int(input.readline())
    s = str(input.readline().rstrip('\n'))
    lis1 = []
    for i,x in enumerate(s):
        if x == '-' or x == ' ':
            lis1.append(i)
    lis1.append(len(s)-1)
    #print lis1

    h = []
    heapq.heappush(h, (-len(lis1), lis1))
    res = []
    res.append(lis1)
    while True:
        if k <=0:
            break
        thisNode = heapq.heappop(h)
        #res.remove(thisNode[1])
        thisNode[1]
        i = bisect.bisect_right(thisNode[1], (thisNode[1][0]+thisNode[1][len(thisNode[1])-1])/2)
        tempL = [thisNode[1][i-1:i][0]+1]
        first = thisNode[1][:i]
        second = tempL+thisNode[1][i:]
        
        heapq.heappush(h, (-(first[len(first)-1]-first[0]), first))
        heapq.heappush(h, (-(second[len(second)-1]-tempL[0]), second))
        #res.append(first)
        #res.append(second)
        k-=1
    maxone = -1
    '''
    
    mineone = min(res)
    mineone.append(0)
    mineone.sort()
    for x in res:
        maxone = max(maxone,x[len(x)-1]-x[0])
    '''
    #print res
    #print h
    
    #heapq.heappush(h, (0, min(h)[1]+[0]))
    
    
    for y,x in h:
        if x[0]==lis1[0]:
            x.append(0)
        x.sort()
        #print x
        maxone = max(maxone,x[len(x)-1]-x[0])
    output = maxone+1
    #-------------------------------OUTPUT----------------------------------
    if os.path.exists('output.txt'):
        open('output.txt', 'w').writelines(str(output))
    else:
        sys.stdout.write(str(output))


if __name__ == "__main__":
    main()

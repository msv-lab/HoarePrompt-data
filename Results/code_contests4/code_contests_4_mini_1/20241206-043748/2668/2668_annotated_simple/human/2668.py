# python2
import sys
import os.path
from collections import deque

def binary_search(num,lis1,low,high):

    while low<=high:
        midone = low+((high-low)/2)
        if num == lis1[midone][0]:
            return (True,lis1[midone][1])
        elif num > lis1[midone][0]:
            low = midone+1
        else:
            high = midone-1
    return (False,-1)




def main():
    if os.path.exists('input.txt'):
        input = open('input.txt', 'r')
    else:
        input = sys.stdin
    #--------------------------------INPUT---------------------------------
    n = int(input.readline())
    init = list(map(int, input.readline().split()))
    init = sorted(init,reverse = True)
    counts = [(1,init[0])]
    #print init
    for i,x in enumerate(init):
        if i ==0:
            continue
        if init[i] == init[i-1]:
            counts.append((counts[len(counts)-1][0]+1,init[i]))
        else:
            counts.append((1,init[i]))
    uniques = []
    for i,x in enumerate(counts):
        if i+1 ==len(counts):
            uniques.append(counts[i])
            break
        if counts[i][1] != counts[i+1][1]:
            uniques.append(counts[i])

    uniques = sorted(uniques,reverse=True)
    #print uniques
    m = int(input.readline())
    audio = list(map(int, input.readline().split()))
    subs = list(map(int, input.readline().split()))
    res,anss = False,0
    audio = [(audio[i],i+1) for i in range(len(audio))]
    audio2 = sorted(audio)
    #print audio2
    for i in range(len(uniques)):
        #print "for :",  uniques[i][1]
        back = binary_search(uniques[i][1],audio2,0,len(audio2)-1)
        if back[0]:
            res = True
            anss = back
            templis = []
            for y in xrange(len(subs)):
                if audio[y][0] == uniques[i][1]:
                    templis.append((subs[y],y+1))
            #print templis
            for z in range(len(uniques)):
                #print "for : ",uniques[z][1]
                back = binary_search(uniques[z][1],templis,0,len(templis)-1)
                #print back
                if back[0]:
                    #print back
                    res = True
                    anss = back
                    break
            break

    if res == False:
        subs = [(subs[i],i+1) for i in range(len(subs))]
        subs = sorted(subs)
        for i in range(len(uniques)):
            back = binary_search(uniques[i][1],subs,0,len(subs)-1)
            if back[0]:
                res = True
                anss = back
                break
    if res:
        output = anss[1]
    else:
        output = 1
    #-------------------------------OUTPUT----------------------------------
    if os.path.exists('output.txt'):
        open('output.txt', 'w').writelines(str(output))
    else:
        sys.stdout.write(str(output))


if __name__ == "__main__":
    main()

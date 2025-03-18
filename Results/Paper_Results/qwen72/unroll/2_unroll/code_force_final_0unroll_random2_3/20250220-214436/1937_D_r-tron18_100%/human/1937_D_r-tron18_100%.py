from itertools import accumulate
 
def last(arr, times):
    n = len(arr)
    return arr[-1] - arr[max(-n, -1-times)]
 
def solve(s1, n):
    pre = [i+1 for i,el in enumerate(s1) if el==">"]
    totalOne = len(pre)
    preOne = list(accumulate(pre, initial=0))
    suffZero = [0]
 
    ans = [0]*n
    for i in range(n-1, -1, -1):
        el = s1[i]
        if el == ">":
            ## this is a one
            ol, zr = totalOne, len(suffZero) - 1
            if ol <= zr:
                ## exit on the left
                zeroInd = 2*last(suffZero, ol)
                oneInd = 2*preOne[-1] - last(preOne, 1)
                ans[i] = zeroInd - oneInd
            else:
                ## exit on the right
                zeroInd = 2*suffZero[-1]
                oneInd = last(preOne, zr) + last(preOne, zr+1)
                oneInd -= last(preOne, 1)
                fi = last(preOne, zr+1) - last(preOne, zr)
                ans[i] = zeroInd - oneInd + n+1 - fi
            preOne.pop()
            totalOne -= 1
        else:
            ## this is a zero
            suffZero.append(suffZero[-1] + i+1)
            ol, zr = totalOne, len(suffZero) - 1
            if zr <= ol:
                ## zr is atleast 1
                ## exit on the right
                zeroInd = suffZero[-1] + suffZero[-2]
                oneInd = 2*last(preOne, zr)
                ans[i] = zeroInd - oneInd + n+1
            else:
                ## exit on the left
                ## ol can be zero
                zeroInd = 2*last(suffZero, ol+1) - last(suffZero, 1)
                oneInd = 2*preOne[-1]
                ans[i] = zeroInd - oneInd
                
    print(*ans)
for case in range(int(input())):
    n = int(input())
    s1 = input()
    solve(s1, n)
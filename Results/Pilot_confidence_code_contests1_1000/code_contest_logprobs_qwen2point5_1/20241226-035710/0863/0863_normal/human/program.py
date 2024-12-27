import sys
input = sys.stdin.readline

############ ---- Input Functions ---- ############
def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))

def main():
    n, x = inlt()
    l = inlt()
    cnt = 0
    tcnt = 0
    for i in xrange(0, n-1):
        if l[i] <= l[i+1]:
            if x < l[i]:
                tcnt += 1
                x = l[i]
        else:
            if x > l[i+1]:
                cnt = -1
                break
            else:
                cnt += tcnt+1
                x = l[i]
                tcnt = 0

    print(cnt)

if __name__ == "__main__":
    for _ in xrange(inp()):
        main()
from sys import stdin, stdout
 
input = stdin.readline
def print(s):
    stdout.write(s+'\n')
    stdout.flush()
 
def q(type, out):
    if type:
        print("! " + ' '.join(map(str, out)))
    else:
        print("? " + ' '.join(map(str, out)))
        res = input().rstrip()
        if res == '-1':
            exit()
        return int(res == "YES")
 
for _ in range(int(input())):
    n = int(input())
 
    if n == -1:
        exit()
 
    l = [[n], [], []]
 
    for i in range(n-1, 0, -1):
        if len(l[2]):
            if q(0, (i, l[2][-1])):
                l[2].append(i)
            elif q(0, (i, l[0][-1])):
                l[0].append(i)
                l[1] += l[2]
                l[2] = []
            else:
                l[1].append(i)
                l[0] += l[2]
                l[2] = []
        else:
            if len(l[1]):
                l[q(0, (i, l[0][-1])) + 2*q(0, (i, l[1][-1])) - 1].append(i)
            else:
                l[1 - q(0, (i, l[0][-1]))].append(i)
 
    ans = [0]*n
    for val in l[0]:
        ans[val-1] = 1
 
    q(1, ans)
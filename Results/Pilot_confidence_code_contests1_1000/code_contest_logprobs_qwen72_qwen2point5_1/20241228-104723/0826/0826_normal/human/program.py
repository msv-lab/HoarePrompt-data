#Finds the fibonacci number, mod 10**13
#http://codeforces.com/problemset/problem/193/E

def test(goal):
    fib=[0,1]
    if goal==0:
        return 0
    if goal==1:
        return 1
    while goal not in fib and fib[-1]<10**13:
        fib.append(fib[-2]+fib[-1])
    if fib[-1]>=10**13:
        return -1
    return fib.index(goal)
        

print(test(int(input())))


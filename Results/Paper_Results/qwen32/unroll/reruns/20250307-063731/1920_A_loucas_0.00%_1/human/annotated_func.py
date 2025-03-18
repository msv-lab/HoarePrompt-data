#State of the program right berfore the function call: t is an integer such that 1 <= t <= 500. Each test case consists of an integer n such that 2 <= n <= 100, followed by n lines each containing two integers a and x where a is in {1, 2, 3} and 1 <= x <= 10^9. There is at least one constraint of type 1 and at least one constraint of type 2 in each test case, and no two constraints are the same.
def func():
    loop = int(input())
    for iterable in range(loop):
        less = []
        
        big = []
        
        no = []
        
        num = 0
        
        innerLoop = int(input())
        
        for iterable2 in range(innerLoop):
            x, a = map(int, input().split())
            if x == 1:
                big.append(a)
            elif x == 2:
                less.append(a)
            else:
                no.append(a)
        
        for i in range(max(big), min(less)):
            if i not in no:
                num = i
                break
        
        print(num)
        
    #State: t is an integer such that 1 <= t <= 500; loop is 0.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a set of constraints. For each test case, it finds and prints an integer that is greater than all constraints of type 1, less than all constraints of type 2, and not listed in any constraints of type 3.


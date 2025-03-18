#State of the program right berfore the function call: t is an integer such that 1 <= t <= 500. For each test case, n is an integer such that 2 <= n <= 100. Each constraint is described by a pair of integers (a, x) where a is an integer in {1, 2, 3} and 1 <= x <= 10^9. There is at least one constraint of type 1 and at least one constraint of type 2. All pairs (a, x) are distinct.
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
        
    #State: A sequence of numbers printed for each iteration of the outer loop, where each number satisfies the conditions specified in the loop.
#Overall this is what the function does:The function reads multiple test cases, each defined by a set of constraints. For each test case, it identifies and prints a number that is greater than the maximum of the 'type 1' constraints and less than the minimum of the 'type 2' constraints, excluding any numbers specified in 'type 3' constraints.


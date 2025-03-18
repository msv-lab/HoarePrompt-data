#State of the program right berfore the function call: t is an integer such that 1 <= t <= 500. For each test case, n is an integer such that 2 <= n <= 100. Each of the following n lines contains two integers a and x, where a is an integer in {1, 2, 3} and 1 <= x <= 10^9. a=1 indicates k must be greater than or equal to x, a=2 indicates k must be less than or equal to x, and a=3 indicates k must be not equal to x. It is guaranteed that there is at least one constraint of type 1 and at least one constraint of type 2, and no two constraints are the same (all pairs (a, x) are distinct).
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
        
    #State: `iterable` is `loop`, `innerLoop` is the value from the last iteration, `iterable2` is `innerLoop - 1` from the last iteration, `big`, `less`, and `no` are the lists from the last iteration, `num` is the first value `i` in the range from `max(big)` to `min(less) - 1` that is not in `no` from the last iteration.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a set of constraints on an integer `k`. For each test case, it determines the smallest integer `k` that satisfies all given constraints and prints this value. The constraints specify that `k` must be greater than or equal to certain values, less than or equal to certain values, and not equal to certain values.


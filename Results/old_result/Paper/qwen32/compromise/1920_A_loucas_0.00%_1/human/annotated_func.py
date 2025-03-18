#State of the program right berfore the function call: Each test consists of multiple test cases. The first line contains a single integer t (1 ≤ t ≤ 500) — the number of test cases. The description of the test cases follows. The first line of each test case contains a single integer n (2 ≤ n ≤ 100) — the number of constraints. The following n lines describe the constraints. Each line contains two integers a and x (a ∈ {1, 2, 3}, 1 ≤ x ≤ 10^9). a denotes the type of constraint. If a=1, k must be greater than or equal to x. If a=2, k must be less than or equal to x. If a=3, k must be not equal to x. It is guaranteed that there is a finite amount of integers satisfying all n constraints (there exists at least one constraint of type 1 and at least one constraint of type 2). It is also guaranteed that no two constraints are the exact same (in other words, all pairs (a, x) are distinct).
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
        
    #State: `loop` is 0, `iterable` is equal to the initial value of `loop`, `innerLoop`, `less`, `big`, `no`, and `num` reflect the state after processing the last test case.
#Overall this is what the function does:The function processes multiple test cases, each defined by a number of constraints. For each test case, it finds and prints the smallest integer `k` that satisfies all the given constraints. The constraints can require `k` to be greater than or equal to a value, less than or equal to a value, or not equal to a value.


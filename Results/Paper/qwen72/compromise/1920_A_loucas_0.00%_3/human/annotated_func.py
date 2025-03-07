#State of the program right berfore the function call: The function `func` is expected to read input from stdin and write output to stdout. The input consists of multiple test cases, where the first line contains a single integer t (1 ≤ t ≤ 500) representing the number of test cases. Each test case starts with a single integer n (2 ≤ n ≤ 100) representing the number of constraints, followed by n lines, each containing two integers a (a ∈ {1, 2, 3}) and x (1 ≤ x ≤ 10^9), where a denotes the type of constraint and x is the value associated with the constraint. It is guaranteed that there is at least one constraint of type 1 and at least one constraint of type 2 in each test case, and no two constraints are the same.
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
        
    #State: The loop will have completed all iterations, with `iterable` equal to `loop - 1` and `num` set to the first value in the range from `max(big)` to `min(less) - 1` that is not in `no` for each test case. If no such value is found in any test case, `num` will remain 0 for that test case.
#Overall this is what the function does:The function `func` reads input from stdin, processes multiple test cases, and writes the output to stdout. Each test case includes constraints of three types (1, 2, and 3) with associated values. The function identifies the first integer within the range from the maximum value of type 1 constraints to the minimum value of type 2 constraints that is not present in the type 3 constraints. If such an integer is found, it is printed; otherwise, 0 is printed. The function completes all test cases, and the final state is that all input has been processed and the corresponding outputs have been written to stdout.


#State of the program right berfore the function call: t is an integer such that 1 <= t <= 500, representing the number of test cases. For each test case, n is an integer such that 2 <= n <= 100, representing the number of constraints. Each constraint is represented by a pair (a, x) where a is an integer in {1, 2, 3} indicating the type of constraint, and x is an integer such that 1 <= x <= 10^9. It is guaranteed that there is at least one constraint of type 1 and at least one constraint of type 2 in each test case, and no two constraints are the same.
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
        
    #State: For each test case, the variable `num` will hold the smallest integer that is greater than or equal to the maximum value in `big` and less than the minimum value in `less`, and is not in the list `no`. If no such integer exists, `num` will be 0. The lists `big`, `less`, and `no` will be empty after each test case. The variable `iterable` will have the value `loop - 1` after the loop completes.
#Overall this is what the function does:The function `func` processes a series of test cases, where each test case is defined by a set of constraints. Each constraint is a pair (a, x), where `a` indicates the type of constraint (1, 2, or 3) and `x` is an integer. The function finds and prints the smallest integer `num` for each test case that meets the following criteria: it is greater than or equal to the maximum value in the list of type 1 constraints (`big`), less than the minimum value in the list of type 2 constraints (`less`), and not present in the list of type 3 constraints (`no`). If no such integer exists, `num` is set to 0. After processing each test case, the lists `big`, `less`, and `no` are reset to empty. The function does not return any value; it only prints the results.


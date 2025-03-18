#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 500, and for each test case, n is an integer such that 2 ≤ n ≤ 100. Each constraint is represented by a pair of integers (a, x) where a ∈ {1, 2, 3} and 1 ≤ x ≤ 10^9. There is at least one constraint of type 1 and one constraint of type 2, and no two constraints are the same.
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
        
    #State: Output State: The output state depends on the inputs provided during each iteration of the loop. For each value of `loop`, the output will be the smallest integer greater than any element in `big` and less than any element in `less`, excluding any elements in `no`. If no such integer exists, the output will be undefined for that iteration.
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it reads a number of constraints. Each constraint is represented by a pair of integers (a, x). The function then determines and prints the smallest integer greater than any element in the 'big' list and less than any element in the 'less' list, excluding any elements in the 'no' list. If no such integer exists, the output for that test case is undefined.


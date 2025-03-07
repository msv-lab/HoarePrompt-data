#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 500, and for each test case, n is an integer such that 2 ≤ n ≤ 100. Each constraint is represented by a pair of integers (a, x) where a ∈ {1, 2, 3} and 1 ≤ x ≤ 10^9, indicating the type of constraint and the value x respectively. There is at least one constraint of type 1 and one constraint of type 2, and no two constraints are the same.
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
        
    #State: After the loop executes all its iterations, `num` will be the smallest integer greater than `max(big)` that is not in the `no` list and also not in the `big` list.
#Overall this is what the function does:The function reads multiple test cases, where each test case includes a number of constraints. For each test case, it identifies the smallest integer greater than the maximum value in the 'big' list that is not present in either the 'big' or 'no' lists and prints this integer. The function does not return any value but prints the result for each test case.


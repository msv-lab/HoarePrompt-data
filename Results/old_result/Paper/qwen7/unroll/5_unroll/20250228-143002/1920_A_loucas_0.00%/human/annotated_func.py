#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 500, each test case contains n constraints where 2 ≤ n ≤ 100, and each constraint is represented by a pair (a, x) where a ∈ {1, 2, 3} and 1 ≤ x ≤ 10^9. There is at least one constraint of type 1 and one constraint of type 2, and no two constraints are the same.
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
        
    #State: Output State: The value of `num` after all iterations of the loop, which is the smallest integer greater than any element in `big` and less than any element in `less`, excluding any elements in `no`. If no such integer exists, `num` remains 0.
#Overall this is what the function does:The function processes multiple test cases, each containing a set of constraints. For each test case, it identifies the smallest integer greater than any number in the 'big' list and less than any number in the 'less' list, while excluding numbers in the 'no' list. If such an integer exists, it is stored in the variable `num`; otherwise, `num` remains 0. Finally, it prints the value of `num` for each test case.


#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 500. For each test case, n is an integer such that 2 ≤ n ≤ 100. There are n lines describing the constraints, where each line contains two integers a and x such that a ∈ {1, 2, 3} and 1 ≤ x ≤ 10^9. Additionally, there is at least one constraint of type 1 and at least one constraint of type 2, and no two constraints are the same.
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
        
    #State: Output State: The output state depends on the input values provided during each iteration of the loop. For each `loop`, the output will be the smallest integer greater than any value in `big` and less than any value in `less`, excluding any values in `no`. If no such integer exists, the output will be undefined for that specific loop iteration.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer t (number of test cases) and an integer n (number of constraints per test case). For each test case, it reads n lines of constraints, where each line contains two integers a and x. Based on the value of a, it categorizes x into either `big`, `less`, or `no`. After processing all constraints, it finds and prints the smallest integer greater than any value in `big` and less than any value in `less`, excluding any values in `no`. If no such integer exists, it prints an undefined value for that test case.


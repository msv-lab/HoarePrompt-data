#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, and each of the four integers p_i in the test cases is an integer such that 0 <= p_i <= 200.
def func():
    for _ in range(int(input())):
        a = list(map(int, input().split()))
        
        cnt = 0
        
        if a[0] % 2 == a[1] % 2 == a[2] % 2 == 1:
            cnt += 1
        
        for x in a:
            cnt += math.floor(x / 2)
        
        print(cnt)
        
    #State: For each test case, the variable `cnt` is printed, which is the sum of 1 (if the first three integers in the list `a` are odd) and the floor division of each integer in the list `a` by 2. The loop iterates `t` times, and for each iteration, a new list `a` is read from input, and a new `cnt` is calculated and printed. The variable `t` is decremented by 1 for each iteration until it reaches 0.
#Overall this is what the function does:The function reads an integer `t` indicating the number of test cases, and for each test case, it reads a list of four integers `a`. It calculates a value `cnt` which is the sum of 1 (if the first three integers in `a` are all odd) and the floor division of each integer in `a` by 2. The function prints `cnt` for each test case. After processing all `t` test cases, the function concludes.


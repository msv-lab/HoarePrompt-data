#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, and for each of the t test cases, X is an integer such that 2 <= X <= 10^18.
def func():
    for i in range(int(input())):
        x = int(input())
        
        max = 100000000
        
        min = -100000000
        
        ans = []
        
        t = 0
        
        while x != 1:
            if x % 2 == 0:
                ans.append(max)
                max -= 1
                x = x // 2
            else:
                ans.append(min)
                min += 1
                x -= 1
            t += 1
        
        ans.reverse()
        
        print(t)
        
        print(*ans)
        
    #State: - The variable `t` will reflect the number of operations (iterations) taken for the last test case to reduce `X` to 1.
    #- The list `ans` will contain the sequence of `max` and `min` values appended during the last test case, reversed.
    #- `max` and `min` will be in their final states after processing the last test case.
    #
    #Since the exact values of `X` for each test case are not provided, we cannot determine the exact numerical values of `t`, `ans`, `max`, and `min`. However, the output state format will be as follows:
    #
    #Output State:
#Overall this is what the function does:The function processes a series of test cases, each involving an integer `X`. For each test case, it performs a series of operations to reduce `X` to 1, appending either a maximum or minimum value to a list based on whether `X` is even or odd. It then outputs the number of operations performed and the sequence of appended values for each test case.


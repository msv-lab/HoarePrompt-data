#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 1000, and for each test case, X is an integer such that 2 ≤ X ≤ 10^{18}.
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
        
    #State: Output State: `i` is 999999, `t` is 100000000, `x` is 1, `max` is -100000000, `min` is 100000000, `ans` is a list containing -100000000 repeated 50000000 times and 100000000 repeated 50000000 times.
    #
    #Explanation: Given the constraints, the maximum value of `x` can be \(10^{18}\). In the worst-case scenario, which is when `x` is always odd, the loop will run until `x` reaches 1. This requires \(100000000\) iterations because the loop increments `min` and decrements `x` by 1 in each iteration, effectively halving the range of values between `max` and `min` each time. Since `t` is incremented in each iteration, it will reach `100000000` after `999999` inputs (as the loop starts from `i=0`). At the end of the loop, `x` will be 1, `max` will be -100000000, `min` will be 100000000, and `ans` will contain `-100000000` repeated 50000000 times followed by 100000000 repeated 50000000 times, as the list `ans` is reversed at the end.
#Overall this is what the function does:The function processes a series of test cases, where for each test case, it calculates the number of steps (`t`) required to reduce an integer `x` (with constraints 2 ≤ `x` ≤ 10^18) to 1 by either dividing it by 2 if even or decrementing it by 1 if odd. It also constructs a list `ans` containing alternating values of a maximum (`max`) and minimum (`min`) integer initialized to 100000000 and -100000000 respectively, and prints both `t` and `ans`. After processing all test cases, the function outputs the total number of steps and the constructed list for each case.


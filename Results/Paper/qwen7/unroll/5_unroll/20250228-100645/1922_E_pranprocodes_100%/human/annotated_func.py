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
        
    #State: Output State: t is the number of steps required to reduce x to 1 by either dividing it by 2 when it is even or decrementing it by 1 when it is odd. For each step, if x was even, max decreases by 1 and ans appends max; if x was odd, min increases by 1 and ans appends min. After the loop, ans is reversed and printed along with t.
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it calculates the number of steps (`t`) required to reduce an integer `x` (2 ≤ x ≤ 10^18) to 1 by either halving it when it is even or decrementing it by 1 when it is odd. During this process, it maintains two values, `max` and `min`, which are updated accordingly. After calculating `t`, it constructs a list `ans` containing these values and prints both `t` and `ans`.


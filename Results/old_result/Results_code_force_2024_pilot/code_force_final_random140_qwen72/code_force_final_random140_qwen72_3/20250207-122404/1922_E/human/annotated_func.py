#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 1000, and X is an integer where 2 ≤ X ≤ 10^18.
def func():
    for i in range(int(input())):
        x = int(input())
        
        max = 100000000
        
        min = -100000000
        
        ans = ''
        
        t = 0
        
        while x != 1:
            if x % 2 == 0:
                ans = f'{max}' + ' ' + ans
                max -= 1
                x = x // 2
            else:
                ans = f'{min}' + ' ' + ans
                min += 1
                x -= 1
            t += 1
        
        print(t)
        
        print(*ans)
        
    #State: After the loop executes all iterations, `t` is the total number of iterations it took for each `x` to become 1 across all test cases, `X` is an integer where 2 ≤ X ≤ 10^18, `i` is the number of test cases (t), `x` is 1, `max` is 100000000 minus the total number of even divisions performed across all test cases, `min` is -100000000 plus the total number of odd decrements performed across all test cases, and `ans` is a string of alternating `max` and `min` values in reverse order of their assignment for each test case, with the final value being either `max` or `min` depending on whether the last `x` value before reaching 1 was even or odd.
#Overall this is what the function does:The function reads an integer `t` indicating the number of test cases, followed by `t` integers `x` (where 2 ≤ x ≤ 10^18). For each `x`, it generates a sequence of numbers by repeatedly dividing `x` by 2 if it is even or decrementing `x` by 1 if it is odd until `x` becomes 1. During this process, it alternates between appending the current maximum (`max`) and minimum (`min`) values to a string `ans`, adjusting `max` and `min` accordingly. After processing each `x`, it prints the total number of steps taken (`t`) and the generated sequence `ans`. The function does not return any value.


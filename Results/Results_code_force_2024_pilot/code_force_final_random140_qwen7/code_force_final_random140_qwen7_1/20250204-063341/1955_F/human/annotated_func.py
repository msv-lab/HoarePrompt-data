#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, p_i is a list of four non-negative integers representing the counts of 1s, 2s, 3s, and 4s in the initial sequence, where 0 ≤ p_i[0] + p_i[1] + p_i[2] + p_i[3] ≤ 200.
def func():
    for i in range(int(input())):
        a, b, c, d = map(int, input().split())
        
        print(a // 2 + b // 2 + c // 2 + d // 2 + int(a % 2 + b % 2 + c % 3 == 3))
        
    #State: Output State: The loop has executed all its iterations, meaning `i` is equal to `t` (the number of test cases), `t` (num_test_cases) is exactly `t`, and it is within the range 1 ≤ t ≤ 10^4. For each test case, `a`, `b`, `c`, and `d` are the integers obtained from the last input before the loop ended. The output of the loop for each test case is calculated as `a // 2 + b // 2 + c // 2 + d // 2 + int(a % 2 + b % 2 + c % 3 == 3)`. All other variables and their states remain unchanged from their final values during the last iteration of the loop.
#Overall this is what the function does:The function processes multiple test cases, each represented by four non-negative integers `a`, `b`, `c`, and `d`, which denote the counts of 1s, 2s, 3s, and 4s in a sequence. For each test case, it calculates and prints a value based on these counts using the formula `a // 2 + b // 2 + c // 2 + d // 2 + int(a % 2 + b % 2 + c % 3 == 3)`. After processing all test cases, the function ends without returning any value.


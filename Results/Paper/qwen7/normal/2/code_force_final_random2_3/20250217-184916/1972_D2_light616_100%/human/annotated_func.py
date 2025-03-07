#State of the program right berfore the function call: n and m are positive integers such that 1 <= n, m <= 2 * 10^6, and n and m are within the limits specified in the problem description.
def func_1():
    x = 1
    cnt = 0
    n, m = map(int, input().split())
    while x * x <= n:
        y = 1
        
        while (x + y) * x <= n and (x + y) * y <= m:
            if math.gcd(x, y) == 1:
                cnt += min(n // ((x + y) * x), m // ((x + y) * y))
            y += 1
        
        x += 1
        
    #State: Output State: `x` is 5, `n` must be at least 64, `m` must be at least 80, `cnt` is 0, `y` is 5.
    #
    #To understand this output state, let's break down the loop and its conditions:
    #
    #1. The loop continues as long as `x * x <= n`.
    #2. For each value of `x`, it initializes `y` to 1 and checks the condition `(x + y) * x <= n` and `(x + y) * y <= m`.
    #3. If both conditions are met and `math.gcd(x, y) == 1`, it increments `cnt` by the minimum of `n // ((x + y) * x)` and `m // ((x + y) * y)`.
    #4. It then increments `y` until the second condition fails.
    #5. Finally, it increments `x` and repeats the process.
    #
    #From the given information:
    #- After the first iteration (`x = 2`), `cnt` is 10.
    #- After the second iteration (`x = 3`), `cnt` is 6.
    #- After the third iteration (`x = 4`), `cnt` is 1.
    #
    #Since `cnt` decreases with each additional iteration, and the loop continues as long as `x * x <= n`, we can infer that `n` must be large enough to allow `x` to reach 5 before the condition `x * x > n` becomes true. Given the pattern, `m` must also be large enough to accommodate the increasing values of `x` and `y`.
    #
    #By the fourth iteration (`x = 5`), the loop will stop because `5 * 5 = 25` which is less than or equal to `n`, but `6 * 6 = 36` which would exceed `n`. At this point, no further contributions to `cnt` are made since `x` has reached the limit where `x * x > n`. Therefore, `cnt` remains at 1 from the third iteration.
    print(cnt)
    #This is printed: 1
#Overall this is what the function does:The function calculates and prints the count of pairs (x, y) such that \(1 \leq x, y\) and \( (x + y) \cdot x \leq n \) and \( (x + y) \cdot y \leq m \), where \( \gcd(x, y) = 1 \). The function reads two integers \(n\) and \(m\) from input, and iterates over possible values of \(x\) and \(y\) to find valid pairs, incrementing a counter for each valid pair found. The function finally prints the total count of such pairs.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n and m are integers such that 1 ≤ n, m ≤ 2⋅10^6, and n + m does not exceed 2⋅10^6 across all test cases.
def func_2():
    t = int(input())
    for _ in range(t):
        func_1()
        
    #State: t must be greater than 2.
#Overall this is what the function does:The function processes a series of test cases, each containing two integers \( n \) and \( m \) such that \( 1 \leq n, m \leq 2 \times 10^6 \) and \( n + m \) does not exceed \( 2 \times 10^6 \). For each test case, it calls another function `func_1()`. After processing all test cases, it ensures that the initial integer \( t \) (indicating the number of test cases) is greater than 2. The function does not return any value.


#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each test case, n and m are integers such that 1 ≤ n, m ≤ 2⋅10^6. It is also guaranteed that the sum of n and the sum of m over all test cases does not exceed 2⋅10^6.
def func_1():
    n, k = map(int, input().split())
    ans = n
    root = int(math.sqrt(n)) + 1
    for i in range(2, root + 1):
        cnt = i * i
        
        ans += (n + i) // cnt
        
    #State: Output State: `i` is greater than `root`; `root` is `int(math.sqrt(n)) + 1`; `cnt` is the last calculated value of `i * i` which is 16; `ans` is the final value calculated after all iterations, which is `n` plus the sum of `(n + i) // cnt` for each `i` from 2 to `root`.
    #
    #To explain this in more detail:
    #- The loop continues as long as `i` is less than or equal to `root`.
    #- After the loop completes, `i` will be greater than `root`.
    #- `root` remains `int(math.sqrt(n)) + 1`.
    #- `cnt` will be the last value of `i * i` used in the loop, which is 16 when `i` was 4.
    #- `ans` is updated in each iteration by adding `(n + i) // cnt`. After all iterations, `ans` will be `n` plus the sum of these additions for each `i` from 2 to `root`.
    print(ans)
    #This is printed: 10
#Overall this is what the function does:The function processes a series of test cases, each containing integers \( n \) and \( m \) (where \( 1 \leq n, m \leq 2 \times 10^6 \)), and calculates a result based on \( n \). Specifically, it initializes \( ans \) to \( n \), then iterates from 2 to \( \sqrt{n} + 1 \), updating \( ans \) by adding \( (n + i) // (i * i) \) for each \( i \). Finally, it prints the computed value of \( ans \).


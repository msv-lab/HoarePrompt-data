#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 500, representing the number of test cases. For each test case, n and k are integers where 1 ≤ n ≤ 100 and 2 ≤ k ≤ 100, representing the number of cards and the number of cards exchanged in each operation, respectively. Additionally, c_1, c_2, ..., c_n are integers where 1 ≤ c_i ≤ 100, representing the numbers on the cards.
def func():
    for _ in range(int(input())):
        n, k = map(int, input().split())
        
        a = list(map(int, input().split()))
        
        h = {}
        
        ans = n
        
        for i in a:
            if i in h:
                h[i] += 1
            else:
                h[i] = 1
            if h[i] >= k:
                ams = k - 1
        
        print(ans)
        
    #State: After all iterations of the loop, `t` is an integer such that 1 ≤ t ≤ 500, `n` and `k` are integers read from the input for each test case, `a` is a list of integers read from the input for each test case, `h` is a dictionary where each key is an integer from the list `a` and its value is the count of occurrences of that integer in `a`, `ans` is set to `n` initially but is updated to `k - 1` if any integer in `a` appears at least `k` times. The final output for each test case is printed as `ans`.
#Overall this is what the function does:The function reads multiple test cases, each consisting of the number of cards (`n`), the number of cards exchanged in each operation (`k`), and the values on the cards (`c_1, c_2, ..., c_n`). For each test case, it counts the occurrences of each card value. If any card value appears at least `k` times, the function sets the result to `k - 1`; otherwise, the result remains `n`. The function prints the result for each test case. After processing all test cases, the function concludes without returning any value.


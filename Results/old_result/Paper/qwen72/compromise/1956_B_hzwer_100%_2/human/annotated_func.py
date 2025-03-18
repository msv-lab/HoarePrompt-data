#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, representing the number of test cases. For each test case, n is an integer such that 1 ≤ n ≤ 2 · 10^5, representing the number of cards each player receives. a_1, a_2, ..., a_n are integers such that 1 ≤ a_i ≤ n, representing the integers on the cards in your hand. Each integer from 1 to n appears at most twice in the sequence a_1, a_2, ..., a_n. The sum of n over all test cases does not exceed 2 · 10^5.
def func():
    input = sys.stdin.readline
    for _ in range(int(input())):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        cnt = [0] * (n + 1)
        
        for x in a:
            cnt[x] += 1
        
        ans = 0
        
        for x in cnt:
            ans += max(0, x - 1)
        
        print(ans)
        
    #State: After all iterations of the loop, `t` is a positive integer such that \(1 \leq t \leq 10^4\). For each of the `t` test cases, `n` is an integer such that \(1 \leq n \leq 2 \cdot 10^5\), `a` is a list of integers provided by the user, `cnt` is a list of integers with length `n + 1` where each element at index `i` in `cnt` represents the count of how many times the integer `i` appears in the list `a`, and `ans` is the sum of `max(0, x - 1)` for all elements `x` in `cnt`. The loop has printed the value of `ans` for each test case.
#Overall this is what the function does:The function reads multiple test cases from standard input. For each test case, it takes an integer `n` and a sequence of integers `a_1, a_2, ..., a_n`. It then counts how many times each integer from 1 to `n` appears in the sequence. The function calculates the sum of the maximum of 0 and the count of each integer minus 1. This sum is printed for each test case. After processing all test cases, the function completes without returning any value.


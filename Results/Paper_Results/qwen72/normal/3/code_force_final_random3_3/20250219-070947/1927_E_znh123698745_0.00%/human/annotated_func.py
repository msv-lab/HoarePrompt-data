#State of the program right berfore the function call: t is a positive integer (1 ≤ t ≤ 10^4), and for each test case, n and k are integers such that 2 ≤ k ≤ n ≤ 2 · 10^5 and k is even.
def func():
    for _ in range(int(input())):
        n, k = map(int, input().split())
        
        array = list(range(1, n + 1))
        
        answer = [1]
        
        a = [1, -1]
        
        for i in range(1, n):
            if (-1) ** i == -1:
                answer.append(array[a[-1]])
                a[-1] -= 1
            else:
                answer.append(array[a[0]])
                a[0] += 1
        
        print(*answer)
        
    #State: `t` is a positive integer (1 ≤ t ≤ 10^4), `_` is `t-1`, `n` is an input positive integer greater than 1, `k` is an input positive integer, `array` is a list of integers from 1 to `n` inclusive, `i` is `n-1`, `answer` is a list containing the integers from 1 to `n` in alternating order starting with 1, and `a` is a list containing the integers `n` and `-n`.
#Overall this is what the function does:The function reads `t` test cases, where `t` is a positive integer (1 ≤ t ≤ 10^4). For each test case, it reads two integers `n` and `k` (2 ≤ k ≤ n ≤ 2 · 10^5 and `k` is even). It then generates a list `answer` containing the integers from 1 to `n` in an alternating order starting with 1. Finally, it prints the contents of `answer` for each test case. The function does not return any value; it only prints the results.


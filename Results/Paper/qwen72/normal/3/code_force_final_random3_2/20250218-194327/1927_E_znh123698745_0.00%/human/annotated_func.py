#State of the program right berfore the function call: t is a positive integer (1 ≤ t ≤ 10^4), n and k are integers for each test case such that 2 ≤ k ≤ n ≤ 2 · 10^5 and k is even.
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
        
    #State: `t` is 0, `n` and `k` are integers provided by the input and must satisfy the initial conditions (2 ≤ k ≤ n ≤ 2 · 10^5 and k is even), `array` is a list of integers from 1 to `n` inclusive, `i` is `n - 1`, `answer` is a list containing the integers from 1 to `n` in alternating order starting with 1, and `a` is a list containing the integers `n` and `-n`.
#Overall this is what the function does:The function `func` processes a series of test cases. Each test case is defined by two integers `n` and `k`, where `2 ≤ k ≤ n ≤ 2 · 10^5` and `k` is even. For each test case, the function generates and prints a list of integers from 1 to `n` in an alternating order starting with 1. The function does not return any value; it only prints the results. After processing all test cases, the function concludes, and the state of the program is such that all test cases have been processed and their results printed.


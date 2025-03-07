#State of the program right berfore the function call: The function `func` is expected to take two parameters, `n` and `k`, where `n` is a positive integer and `k` is a positive even integer such that 2 <= k <= n <= 2 * 10^5. The function should handle multiple test cases, indicated by an integer `t` (1 <= t <= 10^4), which is not explicitly passed as a parameter but is part of the input context.
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
        
    #State: The function `func` will have processed all `t` test cases, and for each test case, it will have printed a sequence of integers from 1 to `n` in a specific alternating pattern. The variables `n`, `k`, `array`, `answer`, and `a` will have been reset and updated for each test case, but their final values will be the state after the last test case has been processed. The loop will have completed all its iterations, and the program will have printed the results for all test cases.
#Overall this is what the function does:The function `func` processes multiple test cases, each defined by two parameters `n` and `k`. For each test case, it generates and prints a sequence of integers from 1 to `n` in a specific alternating pattern. The pattern alternates between taking elements from the end and the beginning of the sequence, starting with the first element. After processing all test cases, the function will have printed the results for each test case, and the internal variables used in the function will be in the state corresponding to the last test case processed.


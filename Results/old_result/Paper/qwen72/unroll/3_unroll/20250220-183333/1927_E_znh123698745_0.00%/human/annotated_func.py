#State of the program right berfore the function call: t is an integer where 1 <= t <= 10^4, n and k are integers for each test case such that 2 <= k <= n <= 2 * 10^5 and k is even.
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
        
    #State: The loop has finished executing for all test cases. For each test case, the output is a sequence of integers from 1 to n, arranged in a specific pattern where the first element is 1, followed by alternating elements from the end and the beginning of the original array. The variables `t`, `n`, and `k` retain their initial values as they are not modified within the loop.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, where `1 <= t <= 10^4`, indicating the number of test cases. For each test case, it reads two integers `n` and `k` from the input, where `2 <= k <= n <= 2 * 10^5` and `k` is even. The function generates and prints a sequence of integers from 1 to `n` for each test case, arranged in a specific pattern: the first element is always 1, followed by alternating elements from the end and the beginning of the original array. The function does not return any value. After the function concludes, the variables `t`, `n`, and `k` retain their initial values as they are not modified within the function.


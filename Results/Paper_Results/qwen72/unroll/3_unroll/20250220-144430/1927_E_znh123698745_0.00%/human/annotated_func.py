#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, n and k are integers for each test case such that 2 <= k <= n <= 2 * 10^5 and k is even.
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
        
    #State: For each test case, the loop prints a sequence of integers from 1 to n, but the sequence alternates between the beginning and the end of the array. The initial state variables `t`, `n`, and `k` remain unchanged, as they are not modified within the loop.
#Overall this is what the function does:The function `func` processes `t` test cases. For each test case, it reads two integers `n` and `k` (where 2 <= k <= n <= 2 * 10^5 and `k` is even) and generates a sequence of integers from 1 to `n`. This sequence alternates between the beginning and the end of the array of integers from 1 to `n`. The function prints this sequence for each test case. The initial state variables `t`, `n`, and `k` remain unchanged.


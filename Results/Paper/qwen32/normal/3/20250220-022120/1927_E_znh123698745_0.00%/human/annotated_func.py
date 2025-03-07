#State of the program right berfore the function call: n and k are integers such that 2 <= k <= n <= 2 * 10^5, k is even, and the sum of n for all test cases does not exceed 2 * 10^5.
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
        
    #State: The sequence `[1, n, 2, n-1, 3, n-2, ..., floor((n+1)/2), ceil((n+1)/2)]` for each test case, printed one per line.
#Overall this is what the function does:The function reads multiple test cases, each consisting of two integers `n` and `k`. For each test case, it generates and prints a sequence of numbers from 1 to `n` in a specific order: starting with 1, then `n`, then 2, then `n-1`, and so on, alternating between the smallest and largest remaining numbers until all numbers are included in the sequence.


#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 10^4. For each of the t test cases, n and k are integers such that 2 <= k <= n <= 2 * 10^5, and k is even. The sum of n across all test cases does not exceed 2 * 10^5.
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
        
    #State: For each test case, the output is a rearranged list of integers from 1 to n, where elements are picked alternately from the start and end of the list.
#Overall this is what the function does:The function processes `t` test cases. For each test case, it takes two integers `n` and `k` (where `2 <= k <= n` and `k` is even) and outputs a rearranged list of integers from 1 to `n`. The rearrangement alternates between picking elements from the start and the end of the list.


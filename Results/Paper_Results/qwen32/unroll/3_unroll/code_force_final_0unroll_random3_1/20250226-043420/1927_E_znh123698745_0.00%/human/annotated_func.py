#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n and k are integers such that 2 <= k <= n <= 2 * 10^5, and k is even. The sum of n across all test cases does not exceed 2 * 10^5.
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
        
    #State: For each test case with given `n` and `k`, the `answer` list will be constructed by alternating between the smallest and largest remaining elements of the initial array `[1, 2, 3, ..., n]`. The variables `t`, `n`, and `k` will remain unchanged except for `answer` being updated for each test case.
#Overall this is what the function does:The function processes multiple test cases, each defined by integers `n` and `k`. For each test case, it constructs a list by alternating between the smallest and largest remaining elements of the initial list `[1, 2, 3, ..., n]` and prints the resulting list. The function does not return any value; it outputs the result directly.


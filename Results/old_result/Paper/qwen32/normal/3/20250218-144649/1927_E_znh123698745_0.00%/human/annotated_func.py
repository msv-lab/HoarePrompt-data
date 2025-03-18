#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 10^4. For each test case, n and k are integers such that 2 <= k <= n <= 2 * 10^5, and k is even. The sum of n across all test cases does not exceed 2 * 10^5.
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
        
    #State: The output state is a sequence of `answer` lists for each test case, where each `answer` list is constructed by starting with 1 and then alternating between the largest and smallest remaining elements of `array` until all elements are included. For each test case, if `n` is odd, the `answer` list is `[1, n, 2, n-1, 3, n-2, ..., n//2, n//2 + 1]`. If `n` is even, the `answer` list is `[1, n, 2, n-1, 3, n-2, ..., n//2 + 1, n//2]`. Each `answer` list is printed on a new line.
#Overall this is what the function does:The function processes multiple test cases, each defined by integers `n` and `k`, where `2 <= k <= n <= 2 * 10^5` and `k` is even. For each test case, it constructs and prints a sequence starting with 1, then alternates between the largest and smallest remaining integers up to `n`, ensuring all integers from 1 to `n` are included in the sequence.


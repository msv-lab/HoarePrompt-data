#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 10^4, and for each test case, n and k are integers such that 2 <= k <= n <= 2 * 10^5, k is even, and the sum of n for all test cases does not exceed 2 * 10^5.
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
        
    #State: For each test case, the output is a line containing the `answer` array constructed by alternating between picking elements from the start and end of the `array` initialized with integers from 1 to `n`.
#Overall this is what the function does:The function processes multiple test cases, each defined by integers `n` and `k`. For each test case, it constructs and prints an array of size `n` by alternating between picking elements from the start and end of an initially sequential array from 1 to `n`. The value of `k` is provided but not used in the current implementation.


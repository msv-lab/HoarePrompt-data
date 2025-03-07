#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4, and for each test case, n and k are integers satisfying 2 ≤ k ≤ n ≤ 2⋅10^5 and k is even.
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
        
    #State: Output State: The output state after the loop executes all its iterations is an `answer` list of length `n-1`. This list is constructed by iterating through the range from 1 to `n-1` and appending elements from the `array` list based on the conditions inside the loop. Specifically, for each odd `i`, the last element of `a` (either `a[-1]` or `a[0]`) is used to index into `array` and append the corresponding element to `answer`. For each even `i`, the first element of `a` (either `a[-1]` or `a[0]`) is adjusted and then used to index into `array` to append the corresponding element to `answer`.
    #
    #After all iterations, `a[-1]` will be reduced to `2-n` and `a[0]` will be increased to `n-1`. Therefore, the `answer` list will contain elements from `array` in a specific pattern determined by these adjustments. The exact elements in `answer` depend on the initial values of `n` and the behavior of the loop, but it will always be a permutation of the elements from 1 to `n` excluding one element, which is 1.
    #
    #For example, if `n=4`, the `answer` list might look like `[1, 4, 3, 2]` or any other permutation of `[2, 3, 4]` since 1 is the first element in `answer` and the rest are derived from `array` based on the loop's conditions.
#Overall this is what the function does:The function processes a series of test cases, each containing integers `n` and `k` (with `2 ≤ k ≤ n ≤ 2⋅10^5` and `k` being even). For each test case, it constructs a list `answer` of length `n-1` by iterating through the range from 1 to `n-1`. During each iteration, it appends elements from a predefined list `array` (containing numbers from 1 to `n`) to `answer` based on specific conditions involving two indices `a[0]` and `a[-1]`. After processing all test cases, it prints the `answer` list for each case. The final state of the program is that it has printed the constructed `answer` lists for all given test cases.


#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 10^4; for each test case, n and k are integers such that 2 <= k <= n <= 2 * 10^5 and k is even.
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
        
    #State: Output State: The loop will execute \(n-1\) times in total. After all iterations, the value of \(i\) will be \(n-1\). The variable `answer` will contain \(n\) elements, starting with 1 and following the pattern described by the loop conditions. Specifically, if \((-1)^i\) is -1, the element at `array[a[-1]]` will be appended to `answer` and `a[-1]` will be decreased by 1. Otherwise, the element at `array[a[0]]` will be appended to `answer` and `a[0]` will be increased by 1. The final state of `a` will be such that `a[0]` is \(n\) and `a[-1]` is 1. The `array` remains unchanged as it is not modified within the loop. The `answer` list will contain elements from the `array` in a specific alternating pattern based on the loop conditions, starting with 1 and ending with either the first or last element of the original `array`, depending on the parity of \(n\).
    #
    #In summary, the final `answer` list will contain \(n\) elements, starting with 1 and following the described pattern, with `a[0]` being \(n\) and `a[-1]` being 1.
#Overall this is what the function does:The function processes multiple test cases, each consisting of two integers \(n\) and \(k\), where \(2 \leq k \leq n \leq 2 \times 10^5\) and \(k\) is even. For each test case, it constructs a list `answer` containing \(n\) elements. Starting with 1, the list follows a specific alternating pattern based on the values of `a[0]` and `a[-1]`. After processing all test cases, the function prints the `answer` list for each case.


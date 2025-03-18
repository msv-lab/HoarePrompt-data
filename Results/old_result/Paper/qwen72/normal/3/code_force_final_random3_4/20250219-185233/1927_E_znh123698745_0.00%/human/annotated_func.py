#State of the program right berfore the function call: The function should take two parameters, n and k, where n and k are integers, 2 ≤ k ≤ n ≤ 2 · 10^5, and k is even.
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
        
    #State: The loop has executed for all iterations, and for each iteration, the `answer` list contains the integers from 1 to `n` in a specific order, which alternates between the first and last elements of the `array` list. The `a` list contains the integers `n` and `0` respectively, and the `array` list remains a list of integers from 1 to `n` inclusive.
#Overall this is what the function does:The function `func` reads an integer from the input, which determines the number of test cases. For each test case, it reads two integers `n` and `k` from the input, where `n` and `k` are integers, 2 ≤ k ≤ n ≤ 2 · 10^5, and `k` is even. It then generates and prints a list `answer` of integers from 1 to `n` in a specific order, alternating between the first and last elements of a sequence. The function does not return any value; it only prints the `answer` list for each test case. After the function concludes, the `answer` list for each test case contains the integers from 1 to `n` in the specified alternating order.


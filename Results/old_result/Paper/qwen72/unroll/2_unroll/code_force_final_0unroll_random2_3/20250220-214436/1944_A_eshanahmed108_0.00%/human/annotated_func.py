#State of the program right berfore the function call: The function `func` is incomplete and does not match the problem description. The correct function definition should be `def min_islands_visitable(n, k):` where `n` is an integer representing the number of islands (1 ≤ n ≤ 100), and `k` is an integer representing the maximum number of bridges that can be destroyed (0 ≤ k ≤ n(n - 1)/2).
def func():
    for _ in range(int(input())):
        n, k = map(int, input().split())
        
        print(n if n - k <= 1 else 1)
        
    #State: The function `min_islands_visitable` is still incomplete and does not match the problem description. The loop has executed all iterations, and for each iteration, it prints `n` if `n - k <= 1` and `1` otherwise. The values of `n` and `k` are not retained after each iteration, so they are not part of the final output state.
#Overall this is what the function does:The function reads an integer indicating the number of test cases. For each test case, it reads two integers `n` and `k` from input, where `n` is the number of islands and `k` is the maximum number of bridges that can be destroyed. It then prints `n` if `n - k` is less than or equal to 1, otherwise it prints 1. The function does not return any value; it only prints the result for each test case. After the function concludes, the input values for `n` and `k` are not retained, and the program state is unchanged except for the printed output.


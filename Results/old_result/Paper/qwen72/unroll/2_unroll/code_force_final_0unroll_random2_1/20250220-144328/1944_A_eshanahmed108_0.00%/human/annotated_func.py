#State of the program right berfore the function call: The function should take two parameters, n and k, where n is an integer representing the number of islands (1 ≤ n ≤ 100) and k is an integer representing the maximum number of bridges that can be destroyed (0 ≤ k ≤ n(n-1)/2).
def func():
    for _ in range(int(input())):
        n, k = map(int, input().split())
        
        print(n if n - k <= 1 else 1)
        
    #State: The loop will print the number of islands (n) if the number of islands minus the number of bridges that can be destroyed (k) is less than or equal to 1. Otherwise, it will print 1. The values of n and k will be read from the input for each iteration, and the loop will execute for the number of times specified by the first input.
#Overall this is what the function does:The function reads a series of inputs, each containing two integers `n` and `k`, where `n` represents the number of islands and `k` represents the maximum number of bridges that can be destroyed. For each input pair, the function prints `n` if `n - k` is less than or equal to 1; otherwise, it prints 1. The function does not return any value. After the function concludes, the input values for `n` and `k` are processed and the corresponding output is printed for each pair.


#State of the program right berfore the function call: The function should take two parameters, n and k, where n is an integer representing the size of the square grid (2 ≤ n ≤ 10^8), and k is an integer representing the minimum number of diagonals that should have at least one colored cell (1 ≤ k ≤ 4n - 2).
def func():
    for _ in range(int(input())):
        n, k = map(int, input().split())
        
        if k == 1:
            print(1)
            continue
        
        if k <= 2 * (n + (n - 2)):
            print(math.ceil(k / 2))
        else:
            print(k // 2 + 1)
        
    #State: The loop will execute for each input pair (n, k) provided, and for each pair, it will print a value based on the conditions specified. The variables n and k will be updated with each iteration based on the input provided, but they will not retain any specific value after the loop completes. The loop will continue to execute until all input pairs have been processed.
#Overall this is what the function does:The function processes multiple pairs of integers (n, k) provided through user input. For each pair, it calculates and prints a value based on the following rules: If k is 1, it prints 1. If k is less than or equal to 2 * (n + (n - 2)), it prints the ceiling of k divided by 2. Otherwise, it prints k divided by 2 plus 1. The function does not return any value; it only prints the calculated results for each input pair. After processing all input pairs, the function concludes, and the variables n and k do not retain any specific values.


#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 1000, and for each test case, n and k are integers such that 2 <= n <= 10^8 and 1 <= k <= 4n - 2.
def func():
    for s in [*open(0)][1:]:
        n, k = map(int, s.split())
        
        print((k // 2 + k % 2) * (k < 4 * n - 3) + 2 * n * (k >= 4 * n - 3) + (k ==
            4 * n - 2))
        
    #State: Output State: The loop will continue to execute for each line of input until there are no more lines to read. For each iteration, `n` and `k` will be updated to the values from the current line of input split by spaces. After all iterations, `s` will be the last line of input (if available), and `n` and `k` will hold the values from the last line of input.
    #
    #In Natural Language: After the loop has executed all its iterations, `n` and `k` will contain the values from the last line of input provided, and `s` will be the last line of input (if any). The loop processes each line of input exactly once, updating `n` and `k` accordingly.
#Overall this is what the function does:The function processes multiple lines of input, each containing two integers \( n \) and \( k \). It calculates and prints a value based on these inputs according to specific conditions. After processing all input lines, the function does not return any value but outputs the calculated results for each line.


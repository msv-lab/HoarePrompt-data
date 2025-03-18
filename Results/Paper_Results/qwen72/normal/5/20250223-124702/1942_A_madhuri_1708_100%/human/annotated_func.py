#State of the program right berfore the function call: The function `func` is incomplete and does not match the problem description. The correct function definition should be `def find_array(n, k):` where `n` and `k` are integers such that 1 ≤ k ≤ n ≤ 10^3.
def func():
    for s in [*open(0)][1:]:
        n, k = map(int, s.split())
        
        if k >= 2:
            if n == k:
                print(*[k for j in range(k)])
            else:
                print('-1')
        else:
            print(*[(j + 1) for j in range(n)])
        
    #State: The loop reads lines from the standard input, processes each line to extract integers `n` and `k`, and prints either a list of `k` integers each equal to `k` if `n == k` and `k >= 2`, or `-1` if `n != k` and `k >= 2`, or a list of integers from 1 to `n` if `k < 2`. The loop continues until all lines from the standard input are processed.
#Overall this is what the function does:The function reads multiple lines from standard input, each containing two integers `n` and `k`. For each line, if `k` is 1 or less, it prints a list of integers from 1 to `n`. If `k` is 2 or more, it prints either `-1` if `n` is not equal to `k`, or a list of `k` integers, each equal to `k`, if `n` is equal to `k`. The function processes all lines until the end of the standard input is reached.


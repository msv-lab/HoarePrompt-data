#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each test case, n is an integer such that 1 ≤ n ≤ 10^9.
def func():
    n_cases = int(input())
    for i in range(n_cases):
        n = int(input())
        
        if n == 1:
            print(1)
        else:
            power = 1
            while power < log2(n):
                power += 1
            if power == n:
                print(2 ** power)
            else:
                power -= 1
                print(2 ** power)
        
    #State: Output State: The value of `t` remains unchanged, and for each `i` from `0` to `n_cases-1`, the program processes an input `n` and prints either `1`, `2 ** power` where `power` is the smallest integer such that `2 ** power >= n` and `power - 1`, depending on whether `n` is `1` or not.
#Overall this is what the function does:The function processes a series of test cases, each containing an integer \( n \) (where \( 1 \leq n \leq 10^9 \)). For each \( n \), it determines and prints either \( 1 \) or \( 2^{\text{power}} \), where \( \text{power} \) is the smallest integer such that \( 2^{\text{power}} \geq n \). The function does not return any value but outputs the results directly.


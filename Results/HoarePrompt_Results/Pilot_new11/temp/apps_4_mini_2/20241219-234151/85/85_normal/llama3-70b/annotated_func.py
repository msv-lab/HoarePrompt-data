#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 10^9.
def func():
    n = int(input())
    ans = 0
    for i in range(1, n // 2 + 1):
        if (i + (n - i)) % 10 ** (len(str(i + (n - i))) - 1) == 0:
            ans += 1
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 2 ≤ n ≤ 10^9, `ans` is the count of valid pairs (i, n - i) where (i + (n - i)) is a multiple of 10 raised to the power of the number of digits in (i + (n - i)) minus 1, `i` is n // 2.
    print(ans)
#Overall this is what the function does:The function reads an integer `n` from input, which should be between 2 and 10^9 inclusive. It then counts how many integer pairs `(i, n - i)` exist for `i` ranging from 1 to `n // 2` such that the sum `i + (n - i)` is a multiple of a power of 10 that corresponds to the number of digits in that sum minus 1. Finally, it prints the count of these valid pairs. Note that the function does not return a value but outputs the result directly via print. There is no handling for invalid input; if the input is outside the specified bounds, the behavior is undefined. Additionally, there's no input mechanism to ensure `n` falls within the required range prior to processing.


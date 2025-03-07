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
        
    #State: Output State: The value of `t` remains unchanged, and for each `i` from `0` to `n_cases-1`, the program processes an input `n` and prints either `1`, `2 ** power`, or `2 ** (power - 1)` based on the conditions provided in the loop. Here, `power` is incremented until it is no longer less than the base-2 logarithm of `n`, and then adjusted if necessary before printing the result.
#Overall this is what the function does:The function processes multiple test cases, each consisting of two integers: t and n. It reads the number of test cases and then for each test case, it reads the value of n. Depending on the value of n, it prints either 1, \(2^{power}\), or \(2^{(power - 1)}\). Here, \(power\) is incremented until it is no longer less than the base-2 logarithm of \(n\), and then adjusted if necessary before printing the result. The function does not return any value; it only prints the results for each test case.


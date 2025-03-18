#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 10^4, and for each test case, x and y are distinct non-negative integers such that 0 <= x, y <= 10^9.
def func():
    for i in range(int(input())):
        n, m = map(int, input().split())
        
        k = abs(n - m)
        
        if k & k - 1 == 0:
            print(k)
        elif n == 0 and m % 2 != 0:
            print(1)
        elif n == 0 and m % 2 == 0:
            print(2)
        else:
            l = bin(k).replace('0b', '')
            p = len(l)
            q = 2 ** (p - 1)
            print(k - q)
        
    #State: Output State: The loop will continue to iterate based on the number of test cases provided as input. For each iteration, the values of `n` and `m` will be read as integers from the user, separated by a space. `k` will be calculated as the absolute difference between `n` and `m`. The output will depend on the value of `k`:
    #
    #- If `k` is a power of 2 (i.e., `k & k - 1 == 0`), the output will be `k`.
    #- If `k` is not a power of 2 and `n` is 0 while `m` is odd, the output will be `1`.
    #- If `k` is not a power of 2 and `n` is 0 while `m` is even, the output will be `2`.
    #- Otherwise, `l` will be the binary string representation of `k` without the '0b' prefix, `p` will be the length of `l`, and `q` will be `2 ** (p - 1)`. The output will be `k - q`.
    #
    #After all iterations of the loop have finished, the output state will include the final values of `n`, `m`, and `k` for each test case, along with the corresponding output printed for each iteration. The variable `i` will be incremented for each iteration but will not affect the final output state.
#Overall this is what the function does:The function processes multiple test cases, each consisting of two distinct non-negative integers `n` and `m`. For each test case, it calculates the absolute difference `k` between `n` and `m`. Based on the value of `k`, it prints one of the following outputs:
- If `k` is a power of 2, it prints `k`.
- If `k` is not a power of 2 and `n` is 0 while `m` is odd, it prints `1`.
- If `k` is not a power of 2 and `n` is 0 while `m` is even, it prints `2`.
- Otherwise, it converts `k` to its binary representation, calculates the highest power of 2 less than or equal to `k`, and prints `k` minus that power of 2.
The function does not return any value but prints the result for each test case.


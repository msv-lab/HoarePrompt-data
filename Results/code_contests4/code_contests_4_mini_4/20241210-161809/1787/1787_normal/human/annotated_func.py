#State of the program right berfore the function call: mod is a positive integer, and the function initializes two lists, fact and ifact, where fact[0] = 1 and ifact[100004] is the modular inverse of fact[100004] under mod. The lists are constructed for values ranging from 0 to 100004.
def func_1():
    fact = [1]
    for i in range(1, 100005):
        fact.append(fact[-1] * i % mod)
        
    #State of the program after the  for loop has been executed: `mod` is a positive integer, `fact` is a list containing the first 100005 factorial values modulo `mod`, `i` is 100004.
    ifact = [0] * 100005
    ifact[100004] = pow(fact[100004], mod - 2, mod)
    for i in range(100004, 0, -1):
        ifact[i - 1] = i * ifact[i] % mod
        
    #State of the program after the  for loop has been executed: `mod` is a positive integer, `fact` is a list containing the first 100005 factorial values modulo `mod`, `i` is 0, `ifact` is a list of length 100005 where `ifact[0]` is equal to `1`, `ifact[1]` is equal to `1`, `ifact[2]` is equal to `2 * ifact[1] % mod`, ..., `ifact[100004]` is equal to `pow(fact[100004], mod - 2, mod)`, and each `ifact[k]` for `k` from 0 to 100004 is computed as `k * ifact[k + 1] % mod`.
    return fact, ifact
    #The program returns the list 'fact' containing the first 100005 factorial values modulo 'mod', and the list 'ifact' where 'ifact[0]' is equal to 1, 'ifact[1]' is equal to 1, 'ifact[2]' is equal to 2 * ifact[1] % mod, ..., and 'ifact[100004]' is equal to pow(fact[100004], mod - 2, mod), with each 'ifact[k]' for k from 0 to 100004 computed as k * ifact[k + 1] % mod.
#Overall this is what the function does:The function initializes and returns two lists: 'fact' which contains the first 100005 factorial values modulo 'mod', and 'ifact' which contains the modular inverses of these factorial values computed using Fermat's Little Theorem. The function does not accept any parameters.

#State of the program right berfore the function call: n is a positive integer, and p is a positive integer greater than 1.
def func_2(n, p):
    return pow(n, p - 2, p)
    #The program returns n raised to the power of (p - 2) modulo p, where n is a positive integer and p is a positive integer greater than 1.
#Overall this is what the function does:The function accepts two parameters, `n` (a positive integer) and `p` (a positive integer greater than 1), and returns `n` raised to the power of `(p - 2)` modulo `p`. There are no edge cases or missing functionalities in the code as it correctly implements the operation as described.

#State of the program right berfore the function call: n is a non-negative integer, r is a non-negative integer such that 0 <= r <= n, fact is a list of precomputed factorials of non-negative integers, and ifact is a list of precomputed modular inverses of those factorials.
def func_3(n, r, fact, ifact):
    t = fact[n] * (ifact[r] * ifact[n - r]) % mod % mod
    return t
    #The program returns t, which is equal to (fact[n] * (ifact[r] * ifact[n - r]) % mod) % mod, where fact is a list of precomputed factorials, ifact is a list of precomputed modular inverses of those factorials, n is a non-negative integer, and r is a non-negative integer such that 0 <= r <= n.
#Overall this is what the function does:The function accepts two non-negative integers `n` and `r`, and two lists `fact` and `ifact` which contain precomputed factorials and their modular inverses, respectively. It calculates and returns the value of `t`, which is derived from the formula `(fact[n] * (ifact[r] * ifact[n - r]) % mod) % mod`. The function assumes that `0 <= r <= n` and that the lists `fact` and `ifact` are appropriately populated for the given inputs.

#State of the program right berfore the function call: The function reads a single line of input and returns a map object containing integers. The input line should consist of space-separated positive integers.
def func_4():
    return map(int, sys.stdin.readline().strip().split())
    #The program returns a map object containing integers from a single line of input consisting of space-separated positive integers.
#Overall this is what the function does:The function reads a single line of input consisting of space-separated integers, converting them to integers and returning a map object containing those integers. It does not handle any edge cases such as empty input or non-integer values, which could lead to runtime errors if the input does not meet the expected format.

#State of the program right berfore the function call: The function reads a line of input and returns a list of integers, where the input line consists of space-separated positive integers.
def func_5():
    return list(map(int, sys.stdin.readline().strip().split()))
    #The program returns a list of integers parsed from a line of space-separated positive integers read from input.
#Overall this is what the function does:The function reads a line of input consisting of space-separated integers and returns a list of those integers. It does not handle any potential errors related to invalid input (e.g., non-integer values) or empty input lines; if such cases occur, the function may raise an exception or return an unexpected result.

#State of the program right berfore the function call: There are multiple test cases represented by the integer t, and for each test case, n is a positive integer (1 ≤ n ≤ 2 ⋅ 10^5), and a is a list of n positive integers where each element a[i] (1 ≤ a[i] ≤ 10^9).
def func_6():
    return sys.stdin.readline().strip()
    #The program returns a single line input read from standard input, stripped of leading and trailing whitespace. This input could be one of the test cases represented by the integer t or any of the positive integers in the list a.
#Overall this is what the function does:The function accepts no parameters and reads a single line of input from standard input, returning it as a string with leading and trailing whitespace removed. This input can be any string including a test case integer or a positive integer from a list.

#State of the program right berfore the function call: x and y are positive integers.
def func_7(x, y):
    while y:
        x, y = y, x % y
        
    #State of the program after the loop has been executed: `y` is 0, `x` is the greatest common divisor (GCD) of the original values of `x` and `y`, since the loop runs until `y` becomes 0. If the original value of `y` was greater than 0, then the loop executed at least once. If the original value of `y` was 0, the loop does not execute, and `x` remains unchanged.
    return x
    #The program returns the greatest common divisor (GCD) of the original values of `x` and `y`, which remains unchanged since `y` is 0.
#Overall this is what the function does:The function accepts two positive integers `x` and `y`, and returns their greatest common divisor (GCD). If `y` is initially 0, the function directly returns `x`, which remains unchanged, effectively returning `x` as the GCD. The function handles cases where `y` is positive, as the loop continues until `y` becomes 0, ensuring the correct GCD is calculated regardless of the initial values.


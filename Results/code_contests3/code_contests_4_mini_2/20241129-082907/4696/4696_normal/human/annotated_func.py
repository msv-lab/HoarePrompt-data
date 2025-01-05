#State of the program right berfore the function call: n is a positive integer such that 1 ≤ n ≤ 50, and m is a positive integer such that 1 ≤ m ≤ cntn, where cntn is the number of permutations of length n with maximum possible value of f(p).
def func():
    a, b = raw_input().split()
    n = int(a)
    i = int(b)
    i = i - 1
    p = range(1, n + 1)
    for k in range(1, n + 1):
        f = factorial(n - k)
        
        d = i // f
        
        print(p[d]),
        
        p.remove(p[d])
        
        i = i % f
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `k` is `n + 1`, `f` is 1, `i` is the final result of the last modification in the loop, `p` is an empty list.
#Overall this is what the function does:The function accepts no parameters and reads two integers from input, `n` (a positive integer between 1 and 50) and `i` (a positive integer representing the index of a permutation). It then calculates and prints the `i`-th permutation of the numbers from 1 to `n` based on the factorial number system. The function does not return a value; it directly prints the result. There is no handling for invalid input cases, such as if `i` exceeds the total number of permutations of `n` (which is `n!`).


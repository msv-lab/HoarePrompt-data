#State of the program right berfore the function call: n and m are positive integers such that 1 ≤ m ≤ cntn, where cntn is the number of permutations of length n with maximum possible value of f(p).**
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
        
    #State of the program after the  for loop has been executed: Output State: `b` is defined, `i` is defined, `n` is greater than or equal to 1, `f` is assigned the value of factorial(0), `d` is assigned the integer division of `i` by `f`, all elements in list `p` are removed one by one in the order specified by `i` divided by `f`.
#Overall this is what the function does:The function `func` reads two integers `a` and `b` from the input, where `a` represents the length of a permutation list `p` and `b` represents an index. It then iterates through the elements of `p` based on calculations involving factorials, integer divisions, and remainders. The function prints elements from `p` based on the calculated indices and removes them sequentially. The final arrangement of printed elements depends on the calculations performed during the loop. The function does not explicitly return a value.


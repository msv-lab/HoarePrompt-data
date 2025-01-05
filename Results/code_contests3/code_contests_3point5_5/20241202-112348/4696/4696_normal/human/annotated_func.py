#State of the program right berfore the function call: n and m are integers such that 1 ≤ m ≤ cntn, where cntn is the number of permutations of length n with maximum possible value of f(p).**
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
        
    #State of the program after the  for loop has been executed: `i` is 0, `n` is greater than or equal to 1, `k` is equal to `n`, `f` is the factorial of 0, `d` is 0, list `p` is empty
#Overall this is what the function does:The function takes user input for integers `a` and `b`, assigns them to `n` and `i` respectively. It then initializes a list `p` with values from 1 to `n`. It iterates over a range from 1 to `n`, calculating the factorial of `n - k`, determining a value `d`, printing an element from list `p` based on `d`, removing that element from `p`, and updating `i`. After the loop, it ensures that `i` is 0, all variables are correctly updated, and the list `p` is empty. The function aims to calculate the number of permutations of length `n` with the maximum possible value of f(p).


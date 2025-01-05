#State of the program right berfore the function call: n and m are integers such that 1 <= m <= cntn, where cntn is the number of permutations of length n with maximum possible value of f(p).**
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
        
    #State of the program after the  for loop has been executed: `n` is at least 1, a and b are valid inputs, m and cntn are integers such that 1 <= m <= cntn, i is an integer value of b decremented by 1, p is an empty list, f is 1, d is 0, i is 0
#Overall this is what the function does:The function accepts user input for integers 'a' and 'b', where 'a' represents the length of permutations and 'b' represents the maximum value. It then calculates the number of permutations of length 'n' with a maximum value of 'm'. The function iterates through the permutations and prints the values accordingly.


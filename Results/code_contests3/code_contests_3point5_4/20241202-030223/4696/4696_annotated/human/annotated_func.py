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
        
    #State of the program after the  for loop has been executed: n is greater than or equal to 1, m and cntn are integers such that 1 ≤ m ≤ cntn, a and b are the values returned by splitting the input, i is 0, p is an empty list, k is n + 1, f is the factorial of 0, d is 0
#Overall this is what the function does:The function `func` reads two integers `n` and `m` from the input and performs calculations on permutations of length `n`. It then prints the values based on those calculations. The code removes the need for the parameter `m` mentioned in the annotations and does not return any value as indicated. The functionality is to manipulate permutations and print specific values based on the calculations without considering the `m` parameter or returning any value.


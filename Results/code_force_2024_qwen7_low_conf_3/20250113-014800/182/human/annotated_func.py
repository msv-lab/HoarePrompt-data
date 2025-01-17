#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4; for each test case, n and m are integers such that 1 ≤ n, m ≤ 2 ⋅ 10^5; a is a binary string of length n; b is a binary string of length m; the sum of all n values does not exceed 2 ⋅ 10^5; the sum of all m values does not exceed 2 ⋅ 10^5.
def func():
    I = input
    for _ in [0] * int(I()):
        I()
        
        a = I() + '*'
        
        k = 0
        
        for x in I():
            k += x == a[k]
        
        print(k)
        
    #State of the program after the  for loop has been executed: `k` is the maximum index where `x == a[k]` holds true for all elements `x` in the iterable returned by `I()`, `a` is a list of length `k+1` ending with `'*'`, `I()` must return an iterable where the length is at least `k+1`, and `k` is printed.
#Overall this is what the function does:The function processes \( t \) test cases. For each test case, it reads a binary string \( a \) of length \( n \) followed by an iterable (likely another binary string or a sequence of characters) using the `input` function. It then iterates over this iterable, comparing each character with the corresponding character in \( a \). If a character in the iterable matches the corresponding character in \( a \), it increments a counter \( k \). After the iteration, it prints the value of \( k \), which represents the maximum index where the condition \( x == a[k] \) holds true for all elements \( x \) in the iterable. If the iterable has fewer than \( k+1 \) elements, the behavior is undefined.


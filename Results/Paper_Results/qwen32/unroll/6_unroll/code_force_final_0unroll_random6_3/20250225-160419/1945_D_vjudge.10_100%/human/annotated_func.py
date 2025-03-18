#State of the program right berfore the function call: pergunta is an integer representing the number of test cases (1 ≤ pergunta ≤ 10^4), a and b are lists of integers where each list contains n integers (1 ≤ a_i, b_i ≤ 10^9), n is an integer representing the number of people in the queue besides Kirill (1 ≤ n ≤ 200,000), and m is an integer representing the maximum allowable final position of Kirill (1 ≤ m ≤ n). The sum of the values of n over all test cases does not exceed 2 · 10^5.
def func_1(pergunta, a, b, n, m):
    x = 0
    for i in range(n - 1, -1, -1):
        if i < m:
            pergunta = min(pergunta, x + a[i])
        
        x += min(a[i], b[i])
        
    #State: pergunta is the minimum value of x + a[i] for all i < m after the loop, x is the sum of min(a[i], b[i]) for all i from 0 to n-1, a and b remain unchanged, n and m remain unchanged.
    print(pergunta)
    #This is printed: pergunta (where pergunta is the minimum value of \( x + a[i] \) for all \( i < m \), and \( x \) is the sum of \(\min(a[i], b[i])\) for all \( i \) from 0 to \( n-1 \))
#Overall this is what the function does:The function `func_1` calculates and prints the minimum value of `x + a[i]` for all `i < m` after processing the lists `a` and `b` and the integer `n`. Here, `x` is the cumulative sum of the minimum values between corresponding elements of `a` and `b` from index `0` to `n-1`. The function does not modify the input lists `a` and `b`, nor the integers `n` and `m`.


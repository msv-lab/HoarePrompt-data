#State of the program right berfore the function call: pergunta is an integer representing the number of test cases (1 \le pergunta \le 10^4), a is a list of n integers (1 \le a_i \le 10^9), b is a list of n integers (1 \le b_i \le 10^9), n is an integer representing the number of people in the queue besides Kirill (1 \le n \le 200,000), and m is an integer representing the maximum allowable final position of Kirill (1 \le m \le n). The sum of the values of n over all test cases does not exceed 2 \cdot 10^5.
def func_1(pergunta, a, b, n, m):
    x = 0
    for i in range(n - 1, -1, -1):
        if i < m:
            pergunta = min(pergunta, x + a[i])
        
        x += min(a[i], b[i])
        
    #State: `pergunta` is the minimum value between the original `pergunta` and the sum of `x` and `a[i]` for all `i` where `i < m`. `x` is the sum of the minimum values between `a[i]` and `b[i]` for all `i` from `n-1` to `0`. `i` is `-1`. The lists `a` and `b`, and the integers `n` and `m` remain unchanged.
    print(pergunta)
    #This is printed: min(original pergunta, x + a[-1]) (where x is the sum of min(a[i], b[i]) for all i from 0 to n-1, and a[-1] is the last element of the list a)
#Overall this is what the function does:The function `func_1` accepts parameters `pergunta`, `a`, `b`, `n`, and `m`. It calculates and prints the minimum value between the original `pergunta` and the sum of `x` and `a[i]` for all `i` where `i < m`, where `x` is the sum of the minimum values between `a[i]` and `b[i]` for all `i` from `n-1` to `0`. The lists `a` and `b`, and the integers `n` and `m` remain unchanged.


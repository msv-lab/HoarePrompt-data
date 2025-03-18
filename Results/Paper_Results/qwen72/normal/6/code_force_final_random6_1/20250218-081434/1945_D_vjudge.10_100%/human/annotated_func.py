#State of the program right berfore the function call: pergunta is an integer representing the number of test cases (1 ≤ pergunta ≤ 10^4), a is a list of n integers (1 ≤ a_i ≤ 10^9), b is a list of n integers (1 ≤ b_i ≤ 10^9), n is a non-negative integer representing the number of people in the queue besides Kirill (1 ≤ n ≤ 200,000), and m is a non-negative integer representing the maximum allowable final position of Kirill (1 ≤ m ≤ n). The sum of n over all test cases does not exceed 2 · 10^5.
def func_1(pergunta, a, b, n, m):
    x = 0
    for i in range(n - 1, -1, -1):
        if i < m:
            pergunta = min(pergunta, x + a[i])
        
        x += min(a[i], b[i])
        
    #State: `pergunta` is the minimum value between the original `perguna` and the sum of `x` and `a[i]` for all `i` where `i < m`. `x` is the sum of `min(a[i], b[i])` for all `i` from `n-1` to `0`. `i` is `-1`. `a` and `b` remain unchanged lists of n integers, `n` is a non-negative integer representing the number of people in the queue besides Kirill (1 ≤ n ≤ 200,000), and `m` is a non-negative integer representing the maximum allowable final position of Kirill (1 ≤ m ≤ n).
    print(pergunta)
    #This is printed: min(perguna, x + a[-1]) (where perguna is the original value of pergunta, x is the sum of min(a[i], b[i]) for all i from 0 to n-1, and a[-1] is the last element of the list a)
#Overall this is what the function does:The function `func_1` takes five parameters: `pergunta` (an integer representing the number of test cases), `a` (a list of integers), `b` (a list of integers), `n` (a non-negative integer representing the number of people in the queue besides Kirill), and `m` (a non-negative integer representing the maximum allowable final position of Kirill). It modifies the value of `pergunta` based on the elements of `a` and `b` and the constraints defined by `m`. The function prints the final value of `pergunta`, which is the minimum value between the original `pergunta` and the sum of `x` and `a[i]` for all `i` where `i < m`, where `x` is the sum of `min(a[i], b[i])` for all `i` from `n-1` to `0`. The lists `a` and `b` remain unchanged, and the function does not return any value.


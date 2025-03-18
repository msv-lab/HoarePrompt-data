#State of the program right berfore the function call: pergunta is an integer representing the number of test cases (1 ≤ pergunta ≤ 10^4), a is a list of n integers where each a_i (1 ≤ a_i ≤ 10^9) represents the cost to bribe the i-th person, b is a list of n integers where each b_i (1 ≤ b_i ≤ 10^9) represents the cost to bribe each person between positions j and i-1 when Kirill moves to position j, n is an integer representing the number of people in the queue (1 ≤ n ≤ 200,000), and m is an integer representing the maximum allowable final position of Kirill (1 ≤ m ≤ n). The sum of n over all test cases does not exceed 2 · 10^5.
def func_1(pergunta, a, b, n, m):
    x = 0
    for i in range(n - 1, -1, -1):
        if i < m:
            pergunta = min(pergunta, x + a[i])
        
        x += min(a[i], b[i])
        
    #State: `pergunta` is the minimum cost required to bribe Kirill to a position less than `m`, `a` and `b` remain unchanged, `n` is the same, `m` is the same, and `x` is the total minimum cost of bribes for all positions from `n-1` to `0`.
    print(pergunta)
    #This is printed: pergunta (where pergunta is the minimum cost required to bribe Kirill to a position less than m)
#Overall this is what the function does:The function `func_1` accepts an integer `pergunta`, two lists of integers `a` and `b`, and two integers `n` and `m`. It calculates and prints the minimum cost required for Kirill to move to a position not exceeding `m` in the queue. The lists `a` and `b` remain unchanged, and the integers `n` and `m` are also unchanged. The function does not return any value.


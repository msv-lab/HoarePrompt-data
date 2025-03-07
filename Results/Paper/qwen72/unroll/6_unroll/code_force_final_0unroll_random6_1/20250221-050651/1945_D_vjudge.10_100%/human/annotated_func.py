#State of the program right berfore the function call: pergunta is an integer representing the number of test cases (1 ≤ pergunta ≤ 10^4), a is a list of n integers where each a_i represents the cost to bribe the i-th person in the queue (1 ≤ a_i ≤ 10^9), b is a list of n integers where each b_i represents the cost to bribe each person between the i-th and the person Kirill is currently bribing (1 ≤ b_i ≤ 10^9), n is an integer representing the number of people in the queue besides Kirill (1 ≤ n ≤ 200,000), and m is an integer representing the maximum allowable final position of Kirill (1 ≤ m ≤ n). The sum of the values of n over all test cases does not exceed 2 · 10^5.
def func_1(pergunta, a, b, n, m):
    x = 0
    for i in range(n - 1, -1, -1):
        if i < m:
            pergunta = min(pergunta, x + a[i])
        
        x += min(a[i], b[i])
        
    #State: pergunta is the minimum cost to bribe people to reach a position up to m, x is the total cost of the minimum bribes from the last person to the first person in the queue.
    print(pergunta)
    #This is printed: pergunta (where pergunta is the minimum cost to bribe people to reach a position up to m)
#Overall this is what the function does:The function `func_1` accepts an integer `pergunta`, a list of integers `a`, a list of integers `b`, an integer `n`, and an integer `m`. It calculates and prints the minimum total cost required for Kirill to bribe people in the queue to reach a position no greater than `m`. The function does not return any value. After the function concludes, `pergunta` is updated to the minimum cost to bribe people to reach a position up to `m`, and `x` is the total cost of the minimum bribes from the last person to the first person in the queue.


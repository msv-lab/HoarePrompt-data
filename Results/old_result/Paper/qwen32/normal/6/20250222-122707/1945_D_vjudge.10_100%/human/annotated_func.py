#State of the program right berfore the function call: pergunta is an integer representing the number of test cases (1 ≤ pergunta ≤ 10^4), a and b are lists of integers where a_i and b_i represent the costs for each person in the queue (1 ≤ a_i, b_i ≤ 10^9), n is the number of people in the queue besides Kirill (1 ≤ n ≤ 200,000), and m is the maximum allowable final position of Kirill (1 ≤ m ≤ n). The sum of the values of n over all test cases does not exceed 2 * 10^5.
def func_1(pergunta, a, b, n, m):
    x = 0
    for i in range(n - 1, -1, -1):
        if i < m:
            pergunta = min(pergunta, x + a[i])
        
        x += min(a[i], b[i])
        
    #State: `pergunta` is the minimum cost of placing Kirill in a position `i < m` with the accumulated minimum costs of all people in the queue up to that point; `x` is the sum of the minimum costs of all people in the queue; `a` and `b` are lists of integers; `n` is the number of people in the queue besides Kirill; `m` is the maximum allowable final position of Kirill.
    print(pergunta)
    #This is printed: pergunta (where pergunta is the minimum cost of placing Kirill in a position i < m with the accumulated minimum costs of all people in the queue up to that point)
#Overall this is what the function does:The function calculates and prints the minimum cost required to position Kirill at a position from 0 to `m` in the queue, considering the costs `a` and `b` for each person in the queue.


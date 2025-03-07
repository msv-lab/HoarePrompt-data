#State of the program right berfore the function call: pergunta is an integer representing the number of test cases, a and b are lists of integers where a_i and b_i represent the costs for Kirill to move past the i-th person in the queue, n and m are integers such that 1 <= m <= n <= 200,000, and the lengths of a and b are both equal to n.
def func_1(pergunta, a, b, n, m):
    x = 0
    for i in range(n - 1, -1, -1):
        if i < m:
            pergunta = min(pergunta, x + a[i])
        
        x += min(a[i], b[i])
        
    #State: Output State: After the loop executes all the iterations, `i` will be `-1`, `pergunta` will be the minimum value it has taken during all iterations (starting from its initial value and updating whenever `x + a[i]` is smaller), and `x` will be the sum of the minimum values between corresponding elements of arrays `a` and `b` from index `n-1` to `m`.
    #
    #In simpler terms, after the loop completes all its iterations, `pergunta` will hold the smallest possible value of `x + a[i]` encountered during the loop, and `x` will be the cumulative sum of the smaller cost between `a[i]` and `b[i]` for each `i` from `n-1` down to `m`.
    print(pergunta)
    #This is printed: pergunta (where pergunta is the minimum value of x + a[i] encountered during the loop)
#Overall this is what the function does:The function processes two lists of integers, `a` and `b`, along with additional parameters `n` and `m`. It calculates the minimum value of `x + a[i]` encountered during a backward iteration through the lists from index `n-1` to `m`. During this process, it also computes the cumulative sum of the minimum values between corresponding elements of `a` and `b` from index `n-1` to `m`. The function prints the minimum value found and returns it as the final output.


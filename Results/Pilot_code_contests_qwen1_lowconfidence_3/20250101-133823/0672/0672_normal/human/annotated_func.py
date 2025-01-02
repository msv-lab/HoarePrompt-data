#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 10^5. The results ai and bi are integers such that 1 ≤ ai, bi ≤ 10^9. Both sequences a1, a2, ..., an and b1, b2, ..., bn are sorted in ascending order.
def func():
    n = int(sys.stdin.readline())
    A = []
    B = []
    T = []
    for i in range(n):
        a, b = map(int, sys.stdin.readline().split())
        
        A.append(a)
        
        B.append(b)
        
        T.append((a, i, 0))
        
        T.append((b, i, 1))
        
    #State of the program after the  for loop has been executed: Output State: `n` is an integer such that \( 1 \leq n \leq 10^5 \), `A` is a list of length `n` containing the integers read from the input, `B` is a list of length `n` containing the integers read from the input, `T` is a list of length \( 2n \) containing tuples of the form `(a, i, 0)` or `(b, i, 1)` where `a` and `b` are the integers read from the input and `i` is the index of the corresponding tuple in the list.
    T.sort()
    a = [0] * n
    b = [0] * n
    for i in range(n // 2):
        a[i] = 1
        
        b[i] = 1
        
    #State of the program after the  for loop has been executed: `n` is an integer such that \(1 \leq n \leq 10^5\), `A` is a list of length `n` containing integers, `B` is a list of length `n` containing integers, `T` is a list of length \(2n\) containing tuples of the form `(a, i, 0)` or `(b, i, 1)` sorted by the first element of each tuple in ascending order, `a` is a list of length `n` with all elements set to 0, `b` is a list of length `n` with all elements set to 0, `i` is `n // 2`.
    for i in range(n):
        if T[i][-1] == 0:
            a[T[i][1]] = 1
        else:
            b[T[i][1]] = 1
        
    #State of the program after the  for loop has been executed: `n` is an integer such that \(1 \leq n \leq 10^5\), `A` is a list of length `n` containing integers, `B` is a list of length `n` containing integers, `T` is a list of length \(2n\) containing tuples of the form `(a, i, 0)` or `(b, i, 1)` sorted by the first element of each tuple in ascending order, `a` is a list of length `n` where `a[j]` is 1 if there exists any tuple `(a, k, 0)` in `T` such that `k == j` and `k >= n // 2`, otherwise `a[j]` is 0, `b` is a list of length `n` where `b[j]` is 1 if there exists any tuple `(b, k, 1)` in `T` such that `k == j` and `k >= n // 2`, otherwise `b[j]` is 0.
    Ans = ''
    for i in range(n):
        Ans += str(a[i])
        
    #State of the program after the  for loop has been executed: `i` is `n`, `n` is an integer such that \(1 \leq n \leq 10^5\), `a` is a list of length `n` with specific values based on `T`, `b` is a list of length `n` with specific values based on `T`, `T` is a list of length \(2n\) with specific tuples based on `A` and `B`, `Ans` is the string "a[0]a[1]...a[n-1]"
    Ans += '\n'
    for i in range(n):
        Ans += str(b[i])
        
    #State of the program after the  for loop has been executed: `i` is `n`, `n` is an integer such that \(1 \leq n \leq 10^5\), `a` is a list of length `n` with specific values based on `T`, `b` is a list of length `n` with specific values based on `T`, `T` is a list of length \(2n\) with specific tuples based on `A` and `B`, `Ans` is the string "a[0]a[1]...a[n-1]\n" + "".join(map(str, b))
    sys.stdout.write(Ans)
#Overall this is what the function does:The function processes two sorted integer sequences \(a_1, a_2, \ldots, a_n\) and \(b_1, b_2, \ldots, b_n\), where \(1 \leq n \leq 10^5\) and \(1 \leq a_i, b_i \leq 10^9\). It reads these sequences from standard input, constructs a list \(T\) of length \(2n\) containing tuples of the form \((a, i, 0)\) or \((b, i, 1)\) based on the input values, sorts \(T\) by the first element of each tuple, and then creates two lists \(a\) and \(b\) of length \(n\) where each element is set to 1 if the corresponding value from the input appears in the second half of the sorted list \(T\). Finally, it outputs a string representation of the lists \(a\) and \(b\) concatenated together, with a newline separating them.


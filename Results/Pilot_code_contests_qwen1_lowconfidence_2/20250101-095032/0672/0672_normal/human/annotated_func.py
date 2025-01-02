#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 10^5. The sequences a1, a2, ..., an and b1, b2, ..., bn are sorted in ascending order, representing the results of the participants in the first and second semifinals respectively.
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
        
    #State of the program after the  for loop has been executed: `n` is an integer within the range 1 ≤ n ≤ 10^5, `A` is a list containing `a1, a2, ..., an` (sorted in ascending order), `B` is a list containing `b1, b2, ..., bn` (sorted in ascending order), `T` is a list containing `(ai, n-1-i, 0)` and `(bi, n-1-i, 1)` for each `i` in the range 0 to n-1.
    T.sort()
    a = [0] * n
    b = [0] * n
    for i in range(n // 2):
        a[i] = 1
        
        b[i] = 1
        
    #State of the program after the  for loop has been executed: `n` is an integer within the range \(1 \leq n \leq 10^5\), `i` is exactly \(\frac{n}{2}\), `A` is a list of integers sorted in ascending order, `B` is a list of integers sorted in ascending order, `T` is a list containing pairs \((a_i, n-1-i, 0)\) and \((b_i, n-1-i, 1)\) for each \(i\) in the range 0 to \(n-1\) and is sorted in ascending order based on the values of \(a_i\) and \(b_i\), `a` is a list of length \(n\) with all elements set to 1, `b` is a list of length \(n\) with all elements set to 1.
    for i in range(n):
        if T[i][-1] == 0:
            a[T[i][1]] = 1
        else:
            b[T[i][1]] = 1
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `i` is `n`, `A` is a list of integers sorted in ascending order, `B` is a list of integers sorted in ascending order, `T` is a list containing pairs \((a_i, n-1-i, 0)\) and \((b_i, n-1-i, 1)\) for each \(i\) in the range 0 to \(n-1\) and is sorted in ascending order based on the values of \(a_i\) and \(b_i\), `a` is a list of length \(n\) with all elements set to 1, and `b` is a list of length \(n\) with all elements set to 1. For each pair \((a_i, n-1-i, 0)\) in `T`, the element at index \(n-1-i\) in `a` is set to 1 if `T[i][-1] == 0`, and for each pair \((b_i, n-1-i, 1)\) in `T`, the element at index \(n-1-i\) in `b` is set to 1.
    Ans = ''
    for i in range(n):
        Ans += str(a[i])
        
    #State of the program after the  for loop has been executed: `Ans` is a string containing the concatenation of the string representations of all elements in the list `a`, `a` retains its original values of all ones, `i` is `n`, and `T` remains unchanged.
    Ans += '\n'
    for i in range(n):
        Ans += str(b[i])
        
    #State of the program after the  for loop has been executed: `Ans` is `"1\n" + str(b[0]) + str(b[1]) + ... + str(b[n-1])`, `i` is `n`, `a` retains its original values of all ones, `T` remains unchanged.
    sys.stdout.write(Ans)
#Overall this is what the function does:The function processes two sorted lists, `A` and `B`, which contain the results of participants in the first and second semifinals respectively. It constructs two new lists, `a` and `b`, both initialized to all ones. It then iterates through a sorted list `T` containing pairs of indices and flags, setting the corresponding elements in `a` and `b` to zero based on the flags. Finally, it concatenates the binary representations of the elements in `a` and `b` into strings and outputs them.


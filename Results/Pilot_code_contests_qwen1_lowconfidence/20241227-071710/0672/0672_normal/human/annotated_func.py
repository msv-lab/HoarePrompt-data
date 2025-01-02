#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 10^5. The results ai and bi are sorted in ascending order for each semifinal, and all results are distinct positive integers not exceeding 10^9.
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
        
    #State of the program after the  for loop has been executed: `n` is an integer such that \(1 \leq n \leq 10^5\); `A` is a list containing integers where each element corresponds to an input `a` in the order they were read; `B` is a list containing integers where each element corresponds to an input `b` in the order they were read; `T` is a list of tuples, where each tuple is in the form `(value, index, flag)`, with `value` being either an element from `A` or `B`, `index` being the index of the element in the original input, and `flag` indicating whether the value comes from `A` (flag = 0) or `B` (flag = 1).
    T.sort()
    a = [0] * n
    b = [0] * n
    for i in range(n // 2):
        a[i] = 1
        
        b[i] = 1
        
    #State of the program after the  for loop has been executed: `n` is at least 2, `A` is a list containing integers, `B` is a list containing integers, `T` is a list of tuples sorted based on the `value` within each tuple, `index` and `flag` values within each tuple remain unchanged, `a` is a list of `n` zeros where `a[i]` is `1` for all `i` in the range `0` to `n // 2 - 1`, `b` is a list of `n` zeros where `b[i]` is `1` for all `i` in the range `0` to `n // 2 - 1`.
    for i in range(n):
        if T[i][-1] == 0:
            a[T[i][1]] = 1
        else:
            b[T[i][1]] = 1
        
    #State of the program after the  for loop has been executed: `n` is at least 2, `i` is `n-1`. For each `i` in the range `0` to `n-1`, if the last element of `T[i]` is 0, then `a[T[i][1]]` is 1; otherwise, `b[T[i][1]]` is 1.
    Ans = ''
    for i in range(n):
        Ans += str(a[i])
        
    #State of the program after the  for loop has been executed: `n` is at least 2, `i` is `n`, `Ans` is the concatenation of the string representations of all elements in the list `a`
    Ans += '\n'
    for i in range(n):
        Ans += str(b[i])
        
    #State of the program after the  for loop has been executed: `n` is at least 2, `i` is equal to `n`, `Ans` is the concatenation of the string representations of all elements in the list `a` followed by a newline character, and then the string representation of each element in the list `b`.
    sys.stdout.write(Ans)
#Overall this is what the function does:The function processes input data consisting of \(n\) pairs of integers \(a_i\) and \(b_i\) where \(1 \leq n \leq 10^5\). It sorts these values into two lists, \(A\) and \(B\), and creates a list \(T\) containing tuples representing each value along with its index and origin (either from \(A\) or \(B\)). After sorting \(T\), it initializes two lists, \(a\) and \(b\), both filled with zeros. For the first half of the sorted values in \(T\), it sets the corresponding indices in \(a\) and \(b\) to 1. Finally, it constructs a string `Ans` by concatenating the binary representations of the lists \(a\) and \(b\) separated by a newline character and outputs this string.


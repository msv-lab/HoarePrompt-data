#State of the program right berfore the function call: n is an integer such that 1 <= n <= 2 * 10^5, and k is an integer such that 0 <= k <= 10^12.
def func_1(n, k):
    k = k // 2
    l = list(range(1, n + 1))
    c = 0
    for i in range(n, -1, -2):
        c += 1
        
        if k == 0:
            return l
        
        if k < i - 1:
            return func_2(c, k, l)
        
        k = k - i + 1
        
        l = func_3(c, l)
        
    #State: The loop will continue to decrement `i` by 2 until `i` is no longer less than or equal to 0. At that point, the function `func_2(c, k, l)` will be returned.
#Overall this is what the function does:The function `func_1` accepts two parameters `n` and `k`. It processes these parameters through a series of conditional checks and function calls. If `k` is zero, it returns the initial list `l`. Otherwise, it iteratively decreases `i` by 2 starting from `n`, updating `c` and `k` accordingly. Depending on the conditions met during each iteration, it either returns the result of `func_2(c, k, l)` or the modified list `l` after calling `func_3(c, l)`. The final state of the program is determined by the specific case that matches the given conditions, ultimately returning either the unchanged initial list `l`, or the result of subsequent function calls involving `c`, `k`, and `l`.

#State of the program right berfore the function call: c is a non-negative integer such that 0 <= c < len(l), k is an integer such that 0 <= k < len(l), and l is a list of integers representing a permutation of length n.
def func_2(c, k, l):
    x, y = l[-c], l[-c - k]
    l[-c], l[-c - k] = y, x
    return l
    #The program returns the list `l` which is a permutation of length n.
#Overall this is what the function does:The function accepts three parameters: `c` (a non-negative integer within the range of the list length), `k` (an integer within the range of the list length), and `l` (a list of integers representing a permutation of length n). It swaps the elements at indices `-c` and `-c-k` in the list `l`. After the swap, the function returns the modified list `l`, which remains a permutation of length n.

#State of the program right berfore the function call: c is an integer such that 1 <= c <= len(l)/2, and l is a list of integers representing a permutation of length n.
def func_3(c, l):
    x, y = l[-c], l[c - 1]
    l[c - 1], l[-c] = x, y
    return l
    #The program returns the list `l` unchanged.
#Overall this is what the function does:The function accepts an integer `c` (where \(1 \leq c \leq \frac{\text{len}(l)}{2}\)) and a list `l` of integers. It swaps the elements at positions `c-1` and `-c` in the list `l`. After performing the swap, it returns the modified list `l`. If no swap is performed (i.e., when the conditions are not met), it still returns the original list `l` unchanged.

#State of the program right berfore the function call: (n, k) are integers such that 1 ≤ n ≤ 2 \cdot 10^{5}, 0 ≤ k ≤ 10^{12}, and k is even if n is odd.
def func_4():
    n, k = map(int, input().split())
    if (k % 2) :
        return 0, 0
        #The program returns two zeros (0, 0)
    #State: `n` is an integer where 1 ≤ n ≤ 2 \cdot 10^{5}; `k` is an integer where 0 ≤ k ≤ 10^{12} and k is odd if n is odd
    if (n % 2) :
        max_k = (n ** 2 - 1) // 2
    else :
        max_k = n ** 2 // 2
    #State: Postcondition: `n` is an integer where 1 ≤ n ≤ 2 \cdot 10^{5}; `k` is an integer where 0 ≤ k ≤ 10^{12}. If `n` is odd, `k` is odd and `max_k` is set to \( n \). If `n` is even, `k` is even and `max_k` is set to \( n \).
    if (max_k < k) :
        return 0, 0
        #The program returns two values, both of which are 0.
    #State: Postcondition: `n` is an integer where \(1 \leq n \leq 2 \cdot 10^5\); `k` is an integer where \(0 \leq k \leq 10^{12}\); `max_k` is set to \(n\).
    return n, k
    #The program returns n, which is an integer between 1 and 200000, and k, which is an integer between 0 and 1000000000000.
#Overall this is what the function does:The function reads two integers \(n\) and \(k\) from input, where \(1 \leq n \leq 2 \cdot 10^5\) and \(0 \leq k \leq 10^{12}\). It checks if \(k\) is odd when \(n\) is odd, and if \(n\) is odd, it calculates the maximum possible value of \(k\) as \(\frac{n^2 - 1}{2}\). If \(k\) exceeds this maximum value, it returns two zeros (0, 0). Otherwise, it returns \(n\) and \(k\). The function can return either two zeros (0, 0) or an integer \(n\) between 1 and 200000 and an integer \(k\) between 0 and 1000000000000.

#State of the program right berfore the function call: l is a list of integers where each integer represents a position in the permutation of length n such that 1 <= l[i] <= n and all positions are distinct.
def func_5(l):
    print('YES')
    #This is printed: YES
    for i in l:
        print(i, end=' ')
        
    #State: Output State: `l` must contain at least one element.
    #
    #Explanation: The loop will continue to execute as long as there are elements in the list `l`. Since the question does not specify any condition that would cause the loop to terminate (such as modifying `l` within the loop to remove elements or setting a break condition), the loop will keep running until `l` is empty. Therefore, after all iterations of the loop have finished, the output state is that `l` must contain at least one element, which in this case would mean `l` is empty. However, based on the given information and the format required, we can only state that `l` must contain at least one element before the loop starts, which remains true even after all iterations.
    print()
    #This is printed: ()
    return
    #The program returns a list `l` that must contain at least one element.
#Overall this is what the function does:The function accepts a list `l` of integers, where each integer represents a position in the permutation of length `n` such that 1 <= l[i] <= n and all positions are distinct. It prints 'YES' followed by the elements of `l` in a single line, then prints an empty tuple `()`. The function ensures that the returned list `l` contains at least one element.

#State of the program right berfore the function call: (n, k) are integers where 1 ≤ n ≤ 2 ⋅ 10^5 and 0 ≤ k ≤ 10^12.
def func_6():
    n, k = func_4()
    if (n == 0) :
        print('NO')
        #This is printed: NO
        return
        #The program returns k, which is an integer between 0 and 10^12
    #State: `n` is an integer between 1 and 2 * 10^5, `k` is an integer between 0 and 10^12, they are the results of `func_4()`. `n` is not equal to 0
    l = func_1(n, k)
    func_5(l)
    return
    #The program returns None
#Overall this is what the function does:The function accepts no parameters and determines whether to return an integer \( k \) between 0 and \( 10^{12} \) or None. If \( n \) (obtained from `func_4()`) is 0, it prints 'NO' and returns. Otherwise, it processes \( n \) and \( k \) using `func_1()` and `func_5()`, then returns None.


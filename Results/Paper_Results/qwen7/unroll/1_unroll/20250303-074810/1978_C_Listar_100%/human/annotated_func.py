#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 2 ⋅ 10^5, and k is an integer such that 0 ≤ k ≤ 10^12.
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
        
    #State: c is 1, k is 0, l is a list containing integers from 1 to n inclusive.
#Overall this is what the function does:The function accepts two parameters, `n` (an integer between 1 and 2⋅10^5) and `k` (an integer between 0 and 10^12). It first halves the value of `k`. Then, it iterates through a list of numbers from 1 to `n`, decrementing `k` and modifying the list `l` based on certain conditions. If `k` reaches 0, it returns the list `l`. Otherwise, it calls another function `func_2` with updated parameters. Finally, the function ensures that `c` is 1, `k` is 0, and `l` contains integers from 1 to `n` inclusive.

#State of the program right berfore the function call: c is a non-negative integer such that 0 <= c < len(l), k is an integer such that 0 <= k < len(l), and l is a list of integers representing a permutation of length n.
def func_2(c, k, l):
    x, y = l[-c], l[-c - k]
    l[-c], l[-c - k] = y, x
    return l
    #The program returns the list `l` which is a permutation of length n.
#Overall this is what the function does:The function accepts three parameters: `c` (a non-negative integer less than the length of the list `l`), `k` (an integer less than the length of the list `l`), and `l` (a list of integers representing a permutation of length `n`). It swaps the elements at indices `-c` and `-c-k` in the list `l`. After the swap, the function returns the modified list `l`, which remains a permutation of length `n`.

#State of the program right berfore the function call: c is a positive integer such that 1 <= c <= len(l)/2, and l is a list of integers representing a permutation of length n.
def func_3(c, l):
    x, y = l[-c], l[c - 1]
    l[c - 1], l[-c] = x, y
    return l
    #The program returns the list `l` with the elements at indices `c - 1` and `-c` swapped.
#Overall this is what the function does:The function accepts two parameters: `c`, a positive integer within the range 1 to half the length of the list `l`, and `l`, a list of integers representing a permutation. It returns the list `l` with the elements at indices `c - 1` and `-c` swapped.

#State of the program right berfore the function call: (n, k) are integers such that 1 ≤ n ≤ 2 \cdot 10^{5}, 0 ≤ k ≤ 10^{12}, and n and k are provided as space-separated values on a single line for each test case.
def func_4():
    n, k = map(int, input().split())
    if (k % 2) :
        return 0, 0
        #The program returns two zeros (0, 0)
    #State: `n` is an integer such that 1 ≤ n ≤ 2 \cdot 10^{5}; `k` is an integer such that 0 ≤ k ≤ 10^{12}; `n` and `k` are assigned the values from the input split and converted to integers. The value of `k` is even
    if (n % 2) :
        max_k = (n ** 2 - 1) // 2
    else :
        max_k = n ** 2 // 2
    #State: Postcondition: `n` is an integer such that 1 ≤ n ≤ 2 \cdot 10^{5}; `k` is an integer such that 0 ≤ k ≤ 10^{12}; `max_k` is the maximum value between `n` and `n` if `n` is odd, and `k` if `n` is even.
    if (max_k < k) :
        return 0, 0
        #The program returns two values both as 0.
    #State: Postcondition: `n` is an integer such that 1 ≤ n ≤ 2 \cdot 10^{5}; `k` is an integer such that 0 ≤ k ≤ 10^{12}; `max_k` is the maximum value between `n` and `n` if `n` is odd, and `k` if `n` is even. **max_k is greater than or equal to k**
    return n, k
    #The program returns the values of `n` and `k`, where `n` is an integer such that 1 ≤ n ≤ 2 * 10^5 and `k` is an integer such that 0 ≤ k ≤ 10^12. The value of `max_k` is the maximum value between `n` (if `n` is odd) and `k` (if `n` is even), and `max_k` is greater than or equal to `k`.
#Overall this is what the function does:The function processes two integers `n` and `k` provided as space-separated values on a single line. It first checks if `k` is odd and returns (0, 0) if true. Then, it calculates the maximum possible value `max_k` based on whether `n` is odd or even. If `max_k` is less than `k`, it returns (0, 0). Otherwise, it returns `n` and `k`.

#State of the program right berfore the function call: l is a list of integers representing a permutation of length n such that the Manhattan value of this permutation is equal to k.
def func_5(l):
    print('YES')
    #This is printed: YES
    for i in l:
        print(i, end=' ')
        
    #State: The numbers in the list l printed in the same order they appear in the list, separated by spaces.
    print()
    #This is printed: \n
    return
    #The program returns nothing
#Overall this is what the function does:The function accepts a list of integers `l` representing a permutation of length `n` with a Manhattan value of `k`. It prints "YES" followed by the elements of the list `l` separated by spaces and then a newline character. The function returns nothing.

#State of the program right berfore the function call: n is a positive integer such that 1 <= n <= 2 * 10^5, and k is an integer such that 0 <= k <= 10^12.
def func_6():
    n, k = func_4()
    if (n == 0) :
        print('NO')
        #This is printed: 'NO'
        return
        #The program returns 0
    #State: `n` is a positive integer such that 1 <= n <= 2 * 10^5, `k` is an integer such that 0 <= k <= 10^12, and `n` is not equal to 0
    l = func_1(n, k)
    func_5(l)
    return
    #The program returns the value of `l` which is the return value of `func_1(n, k)` and is also passed as an argument to `func_5(l)`
#Overall this is what the function does:The function first calls `func_4()` to get values for `n` and `k`. If `n` is 0, it prints 'NO' and returns 0. Otherwise, it calculates a value `l` using `func_1(n, k)`, then passes `l` to `func_5(l)`, and finally returns the value of `l`.


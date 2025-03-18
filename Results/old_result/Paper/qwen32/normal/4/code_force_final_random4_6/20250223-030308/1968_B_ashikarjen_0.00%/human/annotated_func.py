#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n and m are integers such that 1 ≤ n, m ≤ 2 · 10^5. a is a binary string of length n, and b is a binary string of length m. The sum of all n values across test cases does not exceed 2 · 10^5, and the sum of all m values across test cases does not exceed 2 · 10^5.
def func_1():
    n, m = map(int, input().split())
    a = input()
    b = input()
    k = 0
    j = 0
    for i in range(n):
        while j < m and b[j] != a[i]:
            j += 1
        
        if j < m:
            k += 1
            j += 1
        else:
            break
        
    #State: `t` is an integer such that 1 ≤ t ≤ 10^4; `n` and `m` are integers assigned the values from the input, where 1 ≤ n, m ≤ 2 · 10^5; `a` and `b` are binary strings of lengths `n` and `m` respectively; `k` is the number of characters from `a` found in `b` in order; `j` is the index in `b` where the search stopped (either `m` if the loop broke early or the index right after the last matched character if all characters were found).
    print(k)
    #This is printed: k (where k is the number of characters from the binary string `a` found in the binary string `b` in order)
#Overall this is what the function does:The function reads multiple test cases, each consisting of two binary strings `a` and `b`. For each test case, it determines the maximum number of characters from `a` that can be found in `b` in the same order and prints this count.


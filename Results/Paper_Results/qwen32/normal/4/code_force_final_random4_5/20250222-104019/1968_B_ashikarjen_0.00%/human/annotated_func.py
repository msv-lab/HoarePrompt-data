#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n and m are integers such that 1 ≤ n, m ≤ 2 · 10^5. a and b are binary strings of lengths n and m, respectively. The sum of all n values across test cases does not exceed 2 · 10^5, and the sum of all m values across test cases does not exceed 2 · 10^5.
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
        
    #State: `i` is 1, `j` is `m`, and `k` is 0.
    print(k)
    #This is printed: 0
#Overall this is what the function does:The function `func_1` reads two binary strings `a` and `b` of lengths `n` and `m`, respectively, and calculates the maximum number of characters from `a` that can be matched in `b` in order, without reusing characters in `b`. It then prints this count.


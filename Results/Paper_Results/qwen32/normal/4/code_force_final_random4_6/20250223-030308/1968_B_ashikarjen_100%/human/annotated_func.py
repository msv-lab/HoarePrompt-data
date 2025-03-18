#State of the program right berfore the function call: The input consists of an integer t (1 ≤ t ≤ 10^4) representing the number of test cases. For each test case, there are three lines: two integers n and m (1 ≤ n, m ≤ 2 · 10^5) representing the lengths of binary strings a and b, respectively. The next line contains the binary string a of length n, and the following line contains the binary string b of length m. It is guaranteed that the sum of all n values does not exceed 2 · 10^5, and the sum of all m values does not exceed 2 · 10^5.
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
        
    #State: `t`, `n`, `m`, `a`, `b` remain unchanged; `k` is the number of characters in `a` found in `b` in order; `j` is the index in `b` where the search stopped.
    print(k)
    #This is printed: k (where k is the number of characters in `a` found in `b` in order)
    return
    #The program returns None
#Overall this is what the function does:The function `func_1` processes multiple test cases, each consisting of two binary strings `a` and `b`. For each test case, it calculates and prints the number of characters in `a` that can be found in `b` in the same order. The function does not return any value (returns `None`).


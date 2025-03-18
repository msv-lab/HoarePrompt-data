#State of the program right berfore the function call: The input consists of an integer t (1 ≤ t ≤ 10^4) representing the number of test cases. For each test case, there are three lines: two integers n and m (1 ≤ n, m ≤ 2 · 10^5) representing the lengths of binary strings a and b, respectively, followed by the binary string a of length n, and the binary string b of length m. The sum of all n and m across all test cases does not exceed 2 · 10^5.
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
        
    #State: t test cases with n, m, a, b unchanged, k as the count of matched characters, and j as the stopping index in b.
    print(k)
    #This is printed: k (where k is the count of matched characters between some parts of a and b up to the index j)
#Overall this is what the function does:The function reads multiple test cases, each consisting of two binary strings `a` and `b`. For each test case, it counts the maximum number of characters that can be matched sequentially from `a` in `b` and prints this count.


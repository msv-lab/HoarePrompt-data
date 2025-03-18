#State of the program right berfore the function call: The input consists of an integer t (1 ≤ t ≤ 10^4) representing the number of test cases. For each test case, there are three lines: two integers n and m (1 ≤ n, m ≤ 2 · 10^5) representing the lengths of binary strings a and b respectively, followed by the binary strings a and b themselves. The sum of n over all test cases does not exceed 2 · 10^5, and the sum of m over all test cases does not exceed 2 · 10^5.
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
        
    #State: i: index where loop stopped, j: position in b after last match, k: count of matched characters from a in b.
    print(k)
    #This is printed: k (where k is the count of matched characters from list a in list b)
#Overall this is what the function does:The function `func_1` reads multiple test cases, each consisting of two binary strings `a` and `b`. For each test case, it calculates and prints the maximum number of characters from `a` that can appear in `b` in the same order, without reusing characters in `b`.


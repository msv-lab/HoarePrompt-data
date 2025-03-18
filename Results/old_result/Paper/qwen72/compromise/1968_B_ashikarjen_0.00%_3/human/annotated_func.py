#State of the program right berfore the function call: The function should accept two parameters: a list of test cases and the test cases themselves. Each test case consists of two integers n and m, and two binary strings a and b of lengths n and m, respectively. The integers n and m satisfy 1 ≤ n, m ≤ 2 · 10^5, and the total sum of n and m over all test cases does not exceed 2 · 10^5. The binary strings a and b consist only of the characters '0' and '1'.
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
        
    #State: `i` is `n`, `j` is the index of the last character in `b` that matched a character in `a` or `m`, `k` is the number of matches found between characters in `a` and `b` up to the point where `j` reached `m` or the loop completed.
    print(k)
    #This is printed: k (where k is the number of matches found between characters in `a` and `b` up to the point where `j` reached `m` or the loop completed)
#Overall this is what the function does:The function `func_1` reads two integers `n` and `m` from the input, followed by two binary strings `a` and `b` of lengths `n` and `m`, respectively. It then counts the number of matches (`k`) between characters in `a` and `b` by iterating through `a` and finding corresponding characters in `b`. The function prints the count `k` of matches found. The function does not return any value, and it processes one test case at a time. The state after the function concludes is that the input has been consumed, and the count of matches `k` has been printed.


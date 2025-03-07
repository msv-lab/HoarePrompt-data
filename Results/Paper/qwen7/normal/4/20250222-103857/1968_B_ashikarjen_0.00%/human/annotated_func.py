#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n and m are integers such that 1 ≤ n, m ≤ 2 ⋅ 10^5, and a and b are binary strings of lengths n and m respectively. The sum of all n values does not exceed 2 ⋅ 10^5, and the sum of all m values does not exceed 2 ⋅ 10^5.
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
        
    #State: The loop has completed all its iterations, with `j` equal to `m` and `m` greater than 0. For every index `i` ranging from `0` to `n-1`, `b[i]` does not match `a[i]` unless `j` was incremented to `m` before the comparison could be made. The variable `k` contains the count of matches found during the loop's execution.
    print(k)
    #This is printed: 0
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it reads two integers \( n \) and \( m \), followed by two binary strings \( a \) and \( b \) of lengths \( n \) and \( m \) respectively. It then counts the number of positions where the characters in \( a \) and \( b \) match and prints this count. After processing all test cases, the function prints 0.


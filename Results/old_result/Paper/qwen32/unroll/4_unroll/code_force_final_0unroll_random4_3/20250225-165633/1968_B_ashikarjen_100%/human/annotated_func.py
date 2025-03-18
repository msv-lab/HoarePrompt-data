#State of the program right berfore the function call: There are t (1 ≤ t ≤ 10^4) test cases. For each test case, n and m are integers (1 ≤ n, m ≤ 2 · 10^5) representing the lengths of binary strings a and b, respectively. The strings a and b consist only of the characters '0' and '1'. The sum of all n values across test cases does not exceed 2 · 10^5, and the sum of all m values across test cases does not exceed 2 · 10^5.
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
        
    #State: `n` is the first integer input, `m` is the second integer input, `a` is the first input binary string, `b` is the second input binary string, `k` is the count of matched characters in `a` that appear in `b` in the correct order, `j` is the position in `b` where the search stopped.
    print(k)
    #This is printed: - The `print(k)` statement will output the value of `k`, which is the count of matched characters in `a` that appear in `b` in the correct order.
    #
    #Since the exact values of `a` and `b` are not provided, we can't compute the exact numerical value of `k`. However, based on the structure of the problem, the print statement will output the calculated value of `k`.
    #
    #Output:
    return
    #The program returns nothing.
#Overall this is what the function does:The function reads two integers `n` and `m` representing the lengths of two binary strings `a` and `b`. It then counts and prints the number of characters in `a` that appear in `b` in the same order. The function does not return any value.


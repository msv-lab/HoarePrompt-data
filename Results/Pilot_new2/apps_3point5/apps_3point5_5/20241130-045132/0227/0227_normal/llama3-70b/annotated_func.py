#State of the program right berfore the function call: ** n is a positive integer (1 ≤ n ≤ 23), a_k are distinct positive integers (1 ≤ a_k ≤ 10^9).
def func():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    m = 1
    for i in range(1, n):
        if a[i] != a[i - 1] * 2:
            m += 1
        
    #State of the program after the  for loop has been executed: `n` is a positive integer (1 ≤ n ≤ 23), `a` is a list of integers sorted in ascending order. If `a[i]` is not twice the value of `a[i-1]`, `m` is updated to 2, `i` is set to n, and `m` is incremented by 1 for each iteration where the condition is met.
    print(m if m <= 23 else -1)
#Overall this is what the function does:The function `func` reads an integer `n` and a list of `n` integers. It sorts the list, then iterates through the list to count the number of elements that are not twice the previous element. It increments `m` for each such occurrence. After the loop, it prints the final value of `m` if it is less than or equal to 23, otherwise it prints -1. The function does not have explicit return statements.


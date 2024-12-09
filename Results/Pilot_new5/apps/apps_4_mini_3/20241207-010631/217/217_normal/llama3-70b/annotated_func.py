#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 100, and a is a list of n integers where each integer a_i satisfies -100 ≤ a_i ≤ 100.
def func():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    b, c = 0, 0
    for i in range(n):
        if i % 2 == 0:
            b += a[i]
        else:
            c += a[i]
        
    #State of the program after the  for loop has been executed: `b` is the sum of the elements at even indices of `a`, `c` is the sum of the elements at odd indices of `a`, `n` is an input integer satisfying 1 ≤ `n` ≤ 100, `a` is a list of `n` integers sorted in descending order where each integer `a_i` satisfies -100 ≤ `a_i` ≤ 100.
    print(b - c)
#Overall this is what the function does:The function accepts an integer `n` (1 ≤ n ≤ 100) and a list `a` of `n` integers (-100 ≤ a_i ≤ 100). It sorts the list in descending order and then calculates the difference between the sum of the elements at even indices and the sum of the elements at odd indices, finally printing this difference.


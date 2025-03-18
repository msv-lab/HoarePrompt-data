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
        
    #State of the program after the  for loop has been executed: `n` is an integer where \(1 \leq n \leq 100\), `a` is a list of `n` integers sorted in descending order, `b` is the sum of elements at even indices of `a`, `c` is the sum of elements at odd indices of `a`.
    print(b - c)
#Overall this is what the function does:The function accepts a list of integers `a` where the length `n` is an integer between 1 and 100, inclusive, and each element in the list satisfies -100 ≤ a_i ≤ 100. The function sorts the list in descending order and then calculates the difference between the sum of elements at even indices and the sum of elements at odd indices. The function prints this difference.


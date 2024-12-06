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
        
    #State of the program after the  for loop has been executed: `b` is equal to the sum of all elements at even indices of `a`, `c` is equal to the sum of all elements at odd indices of `a`, `n` is an integer such that 1 ≤ `n` ≤ 100, `a` is a list of `n` integers sorted in reverse order.
    print(b - c)
#Overall this is what the function does:The function accepts an integer `n` (where 1 ≤ n ≤ 100) and a list `a` of `n` integers (each in the range -100 to 100). It sorts the list `a` in descending order and calculates the difference between the sum of integers at even indices and the sum of integers at odd indices, then prints this difference.


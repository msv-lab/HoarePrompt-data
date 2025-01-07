#State of the program right berfore the function call: n is a positive integer such that 1 ≤ n ≤ 100, and a is a list of n integers where each integer a_i satisfies -100 ≤ a_i ≤ 100.
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
        
    #State of the program after the  for loop has been executed: `b` is the sum of elements in `a` at even indices, `c` is the sum of elements in `a` at odd indices, and `a` is a list of integers sorted in reverse order.
    print(b - c)
#Overall this is what the function does:The function accepts a positive integer `n` and a list `a` of `n` integers, sorts the list in descending order, and calculates the difference between the sum of integers at even indices and the sum of integers at odd indices. It then prints this difference. The function does not return any value; it only outputs the result to the console.


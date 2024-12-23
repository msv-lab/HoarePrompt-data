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
        
    #State of the program after the  for loop has been executed: `i` is `n`, `b` is the sum of every even-indexed element in `a`, `c` is the sum of every odd-indexed element in `a`, `n` is a positive integer within the range 1 ≤ n ≤ 100, `a` is a list of `n` integers sorted in descending order, each integer in the list satisfies -100 ≤ a_i ≤ 100, `b` is 0, `c` is 0.
    print(b - c)
#Overall this is what the function does:The function `func` accepts a list of integers `a` of length `n` (where `1 ≤ n ≤ 100`) and each integer in the list satisfies `-100 ≤ a_i ≤ 100`. After sorting the list in descending order, the function calculates the sum of elements at even indices (`b`) and the sum of elements at odd indices (`c`). Finally, it prints the difference between these two sums (`b - c`). The function does not return any value; instead, it only prints the result of `b - c`.


#State of the program right berfore the function call: The input is a sequence of integers, where the first integer represents the number of elements in the sequence (n), and the subsequent integers represent the elements of the sequence (a_1, a_2,..., a_{n}), such that 1 ≤ n ≤ 100 and -100 ≤ a_{i} ≤ 100.
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
        
    #State of the program after the  for loop has been executed: `n` is an integer between 1 and 100 (inclusive), `a` is a list of `n` integers between -100 and 100 (inclusive), sorted in descending order, `b` is the sum of elements at even indices in `a`, `c` is the sum of elements at odd indices in `a`.
    print(b - c)
#Overall this is what the function does:The function accepts a sequence of integers as input, where the first integer represents the count of subsequent integers, sorts these integers in descending order, calculates the sum of elements at even indices and the sum of elements at odd indices, and then prints the difference between these two sums, without explicit validation for input format or range, assuming the input adheres to specified constraints.


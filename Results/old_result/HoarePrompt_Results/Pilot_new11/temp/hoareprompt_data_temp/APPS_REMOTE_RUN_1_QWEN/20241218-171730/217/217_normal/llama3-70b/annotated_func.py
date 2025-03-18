#State of the program right berfore the function call: The input consists of two lines. The first line contains one integer n (1 ≤ n ≤ 100) representing the number of elements in the sequence a, and the second line contains n integers a_1, a_2, ..., a_n ( - 100 ≤ a_i ≤ 100) representing the elements of the sequence a.
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
        
    #State of the program after the  for loop has been executed: - `b` is the sum of all elements in `a` at even indices.
    #- `c` is the sum of all elements in `a` at odd indices.
    #- `i` is `n-1`.
    #- `a` remains a list of `n` integers sorted in descending order.
    #- `n` is an integer between 1 and 100 (inclusive).
    #
    #Output State:
    print(b - c)
#Overall this is what the function does:The function reads an integer \( n \) and then reads \( n \) integers from the input. It sorts these integers in descending order and then calculates the difference between the sum of elements at even indices and the sum of elements at odd indices. The function prints this difference. The function does not return any value. Potential edge cases include when \( n \) is 1, in which case both sums would be zero, resulting in an output of 0. There is no missing functionality noted in the provided code.


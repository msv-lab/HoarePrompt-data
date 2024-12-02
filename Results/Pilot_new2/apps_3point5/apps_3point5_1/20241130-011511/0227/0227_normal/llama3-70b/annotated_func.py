#State of the program right berfore the function call: **Precondition**: **n is a positive integer (1 ≤ n ≤ 23) and a_k (1 ≤ a_k ≤ 10^9) are distinct positive integers.**
def func():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    m = 1
    for i in range(1, n):
        if a[i] != a[i - 1] * 2:
            m += 1
        
    #State of the program after the  for loop has been executed: n is at least 2, i is n, a_k (1 ≤ a_k ≤ 10^9) are distinct positive integers, a is a list of integers obtained by splitting the input and sorted in ascending order, m is the number of times a[i] is not equal to twice the value of a[i - 1] + 1.
    print(m if m <= 23 else -1)
#Overall this is what the function does:The function `func` reads an integer `n` and a list of integers `a`, then sorts the list `a`. It iterates over the sorted list and increments `m` by 1 every time an element `a[i]` is not twice the value of the previous element `a[i-1] + 1`. Finally, it prints the value of `m` if it is less than or equal to 23; otherwise, it prints -1. The function does not accept any parameters explicitly and works based on user input.


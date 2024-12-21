#State of the program right berfore the function call: The input consists of two lines: the first line contains an integer n, and the second line contains n integers. n is an integer such that 1 <= n <= 100, and the integers in the second line are also integers such that -100 <= a_i <= 100 for 1 <= i <= n.
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
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 1 <= `n` <= 100, `a` is a sorted list of input integers in descending order, `b` is the sum of elements at even indices of `a` up to `n-1`, `c` is the sum of elements at odd indices of `a` up to `n-1`.
    print(b - c)
#Overall this is what the function does:The function accepts no explicit parameters and reads input for an integer n and n subsequent integers, performs sorting in descending order on the input integers, calculates the sum of elements at even and odd indices separately, and then prints the difference between the sum of elements at even indices and the sum of elements at odd indices. The final state of the program includes the input integer n and the n input integers being consumed, resulting in a program output that represents the calculated difference between the two sums, covering all potential cases within the given constraints of 1 <= n <= 100 and -100 <= a_i <= 100 for 1 <= i <= n, including edge cases where n equals 1 or equals 100, and handling both positive and negative input integers.


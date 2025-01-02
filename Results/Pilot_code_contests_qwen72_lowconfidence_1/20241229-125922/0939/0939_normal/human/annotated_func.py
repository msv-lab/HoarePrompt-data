#State of the program right berfore the function call: N is an integer such that 2 ≤ N ≤ 10^5, and A is a list of N integers where each integer A_i satisfies 1 ≤ A_i ≤ 10^9.
def func():
    N = int(raw_input())
    A = list(map(int, raw_input().split(' ')))
    cnt = 0
    for a in A:
        cnt += 1 if a & 1 == 1 else 0
        
    #State of the program after the  for loop has been executed: `N` is an input integer such that 2 ≤ N ≤ 10^5, `A` is a list of N integers where each integer \( A_i \) satisfies 1 ≤ \( A_i \) ≤ 10^9, `cnt` is the number of odd integers in the list `A`.
    print('YES' if cnt % 2 == 0 else 'NO')
#Overall this is what the function does:The function reads an integer `N` and a list `A` of `N` integers from the standard input. It then counts the number of odd integers in the list `A`. If the count of odd integers is even, the function prints "YES"; otherwise, it prints "NO". The function does not return any value. The state of the program after the function concludes includes the following: `N` is an integer such that 2 ≤ N ≤ 10^5, `A` is a list of `N` integers where each integer \( A_i \) satisfies 1 ≤ \( A_i \) ≤ 10^9, and the output is either "YES" or "NO" based on the parity of the count of odd integers in `A`. Edge cases include when `N` is 2 (the minimum allowed value) and when all integers in `A` are even or all are odd.


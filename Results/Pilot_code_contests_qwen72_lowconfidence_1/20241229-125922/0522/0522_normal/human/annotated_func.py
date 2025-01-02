#State of the program right berfore the function call: b is an integer such that 2 ≤ b ≤ 100, k is an integer such that 1 ≤ k ≤ 10^5, and a is a list of k integers where 0 ≤ a[i] < b for all i. The list a does not contain leading zeros unless k = 1.
def func_1():
    b, k = map(int, input().split())
    a = list(map(int, input().split()))
    n = k % 2
    m = a[-1] % 2
    if (n == 1) :
        for i in a[:-1]:
            if i % 2 == 1:
                m = not m
            
        #State of the program after the  for loop has been executed: `b` is an integer input, `k` is an integer input, `a` is a list of integers read from input that does not contain leading zeros unless the length of `a` is 1, `n` is 1, `m` is `a[-1] % 2` if the number of odd numbers in `a[:-1]` is even, otherwise `m` is `not (a[-1] % 2)`.
    #State of the program after the if block has been executed: *`b` is an integer input, `k` is an integer input, `a` is a list of integers read from input that does not contain leading zeros unless the length of `a` is 1, `n` is `k % 2`, `m` is `a[-1] % 2`. If `n` == 1 and the number of odd numbers in `a[:-1]` is even, `m` is `a[-1] % 2`. Otherwise, if `n` == 1 and the number of odd numbers in `a[:-1]` is odd, `m` is `not (a[-1] % 2)`.
    print('odd' if m else 'even')
#Overall this is what the function does:The function `func_1` reads two integers `b` and `k` from the input, followed by a list of `k` integers `a`. It then determines whether the sum of the elements in `a` is odd or even. Specifically, it checks the parity of the last element `a[-1]` and toggles this parity based on the number of odd elements in the rest of the list `a[:-1]` if `k` is odd. Finally, it prints 'odd' if the resulting parity is odd, and 'even' otherwise. The function does not return any value. Note that the function assumes the input constraints: 2 ≤ b ≤ 100, 1 ≤ k ≤ 10^5, and 0 ≤ a[i] < b for all i, with no leading zeros unless k = 1.


#State of the program right berfore the function call: The number of test cases T is a positive integer such that 1 ≤ T ≤ 10. Each test case consists of two integers n (2 ≤ n ≤ 1000) and m (1 ≤ m ≤ n), followed by a list of n non-negative integers representing the weights of fridges, each weight a_i satisfying 0 ≤ a_i ≤ 10^4.
def func_1():
    n, m = list(map(int, le.pop().split()))
    a = list(map(int, le.pop().split()))
    if (m < n or n == 2) :
        af.append(-1)
        return None
        #The program returns None
    #State of the program after the if block has been executed: *`n` is the first integer from the last element of `le`, `m` is the second integer from the last element of `le`, and `a` is a list of integers created from this last element of `le` after splitting it. The value of `m` is greater than or equal to `n` and `n` is not equal to 2.
    af.append(2 * sum(a))
    for k in range(n):
        af.append(str(k + 1) + ' ' + str((k + 1) % n + 1))
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `k` is `n - 1`, `af` contains `n` strings in the format of `'i (i % n + 1)'` for `i` from `1` to `n`.
#Overall this is what the function does:The function accepts no parameters and processes input to handle test cases involving two integers, `n` and `m`, followed by a list of weights. If `m` is less than `n` or `n` equals 2, it appends -1 to a list and returns None. Otherwise, it appends twice the sum of the weights to the list and generates `n` strings formatted as `'i (i % n + 1)'`, where `i` ranges from 1 to `n`. The function does not return any value, and its primary output is through the `af` list.


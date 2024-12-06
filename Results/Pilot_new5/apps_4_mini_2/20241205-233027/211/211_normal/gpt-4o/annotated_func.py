#State of the program right berfore the function call: n is a positive integer such that 1 ≤ n ≤ 100, and A is a list of n integers where each integer a_i satisfies -1000 ≤ a_i ≤ 1000.
def func():
    n = int(input())
    A = list(map(int, input().split()))
    total_sum = sum(A)
    if (total_sum != 0) :
        print('YES')
        print('1')
        print('1', n)
    else :
        for i in range(n):
            if A[i] != 0:
                print('YES')
                print('2')
                print('1', i + 1)
                print(i + 2, n)
                break
            
        #State of the program after the  for loop has been executed: `total_sum` is 0, `A` is a list of `n` integers that sum to 0, `n` is greater than 0, and `A` contains only zeros. If all elements in `A` are zero, 'NO' is printed, and the loop does not execute; hence `i` will be equal to `n`.
    #State of the program after the if-else block has been executed: *`n` is an input positive integer such that 1 ≤ `n` ≤ 100; `A` is a list of `n` integers where each integer `a_i` satisfies -1000 ≤ `a_i` ≤ 1000; `total_sum` is equal to `sum(A)`. If `total_sum` is not equal to 0, the output is '1', and `n` remains the input positive integer. If `total_sum` is equal to 0, then `A` consists only of zeros, and 'NO' is printed without executing the loop, resulting in `i` being equal to `n`.
#Overall this is what the function does:The function accepts a positive integer `n` (1 ≤ n ≤ 100) and a list `A` of `n` integers, each of which lies within the range -1000 to 1000. It computes the sum of the integers in `A`. If the sum is not equal to 0, it prints 'YES', followed by '1' and the value of `n`. If the sum is equal to 0 and at least one integer in `A` is non-zero, it prints 'YES', then '2', followed by two ranges: one starting from index 1 to the first non-zero element and the second from the next index to `n`. If all elements in `A` are zero, it prints 'NO'. The function does not handle unexpected input types or values outside the specified ranges.


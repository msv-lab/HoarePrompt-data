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
            
        #State of the program after the  for loop has been executed: `n` is a positive integer where 1 ≤ `n` ≤ 100, `total_sum` is 0, and `i` is `n-1`. The printed output is 'NO' indicating all elements in A are zero.
    #State of the program after the if-else block has been executed: *`n` is a positive integer where 1 ≤ `n` ≤ 100; `A` is a list of `n` integers satisfying -1000 ≤ a_i ≤ 1000; if `total_sum` is not equal to 0, 'YES' and '1' are printed, followed by the values of `1` and `n`. If `total_sum` is equal to 0, 'NO' is printed, indicating that all elements in `A` are zero.
#Overall this is what the function does:The function accepts a positive integer `n` (where 1 ≤ `n` ≤ 100`) and a list `A` of `n` integers (each between -1000 and 1000). It calculates the sum of the elements in `A`. If the sum is not zero, it prints 'YES', followed by '1' and the values '1' and `n`. If the sum is zero, it checks each element in `A`; if it finds a non-zero element at index `i`, it prints 'YES', followed by '2', then prints '1' and `i + 1`, and finally prints `i + 2` and `n`. If all elements in `A` are zero, it prints 'NO'.


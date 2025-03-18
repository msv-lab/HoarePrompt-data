#State of the program right berfore the function call: n is a positive integer (1 ≤ n ≤ 100), A is a list of n integers where each integer a_i satisfies -1000 ≤ a_i ≤ 1000.
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
            
        #State of the program after the  for loop has been executed: if all elements in `A` are 0, then `A` is all zeros; otherwise, `A` contains at least one non-zero element, `n` is greater than 0, and `total_sum` is 0.
    #State of the program after the if-else block has been executed: *`A` is a list of integers satisfying -1000 ≤ a_i ≤ 1000, `n` is the length of `A`, and `total_sum` is equal to `sum(A)`. If `total_sum` is not equal to 0, 'YES', '1', and the values of '1' and `n` have been printed. If `total_sum` is equal to 0, then all elements in `A` are 0; otherwise, `A` contains at least one non-zero element, `n` is greater than 0, and `total_sum` equals 0.
#Overall this is what the function does:The function reads a positive integer `n`, which specifies the length of a list `A` containing `n` integers, with each integer in the range of -1000 to 1000. It calculates the sum of the integers in list `A`. If the sum is not zero, it prints "YES", followed by "1", and the values "1" and `n`, indicating that a non-zero sum was found. If the sum is zero, it checks for non-zero elements in `A`. If it finds one, it prints "YES", followed by "2", and the indices of the first non-zero element (1-based index) and a range from the next index to `n`. If all elements are zero, the function does not provide any output. The overall state of the program after execution is that it will either confirm the presence of non-zero sums or indicate that all elements are zero without a specific output.


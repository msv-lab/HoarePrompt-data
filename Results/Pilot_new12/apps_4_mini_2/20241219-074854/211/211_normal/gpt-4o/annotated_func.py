#State of the program right berfore the function call: n is a positive integer (1 ≤ n ≤ 100) representing the number of elements in the array A, and A is a list of n integers where each integer satisfies -1000 ≤ a_i ≤ 1000.
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
            
        #State of the program after the  for loop has been executed: `total_sum` is equal to 0, `A` is a list of `n` integers, `n` is a positive integer (1 ≤ n ≤ 100). If at least one element in `A` is not 0, it would print 'YES' followed by '2', '1', and the index of the non-zero element. If all elements in A are 0, it will print 'NO'.
    #State of the program after the if-else block has been executed: *`n` is a positive integer (1 ≤ n ≤ 100), `A` is a list of `n` integers, and `total_sum` is the sum of elements in `A`. If `total_sum` is not equal to 0, then "1" is printed followed by the value of `n`. If `total_sum` is equal to 0, then if at least one element in `A` is not 0, it prints 'YES' followed by '2', '1', and the index of the non-zero element. If all elements in `A` are 0, it prints 'NO'.
#Overall this is what the function does:The function reads a positive integer n, representing the number of elements in an integer list A, which contains n integers ranging from -1000 to 1000. It calculates the sum of the elements in A. If the total sum is non-zero, it prints 'YES', '1', and the total number of elements n. If the total sum is zero, it looks for the first non-zero element in A. If a non-zero element is found, it prints 'YES', '2', '1', and the index of the non-zero element (1-based), followed by the indices from the next element to n. If all elements in A are zero, it prints 'NO'. In summary, the function outputs whether a valid non-zero sequence can be established from the list A, handling both scenarios where the sum is zero or non-zero. Additionally, it contains a potential edge case where if all elements are zero, it explicitly prints 'NO', which may not have been adequately highlighted in the annotations.


#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 100, and the list A consists of n integers where each integer a_i satisfies -10^3 ≤ a_i ≤ 10^3.
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
            
        #State of the program after the  for loop has been executed: `n` is an integer such that \( 1 \leq n \leq 100 \); `A` is a list of `n` integers; `total_sum` is 0; if the loop executes, `i` is the index of the first non-zero element in `A`, and the statements 'YES', '2', '1 i+1', 'i+2 n' are printed; if the loop does not execute, `i` is `n`, and 'NO' is printed.
    #State of the program after the if-else block has been executed: *`n` is an integer such that \(1 \leq n \leq 100\); `A` is a list of `n` integers; `total_sum` is the sum of all elements in `A`. If `total_sum` is not zero, the printed output is '1' and `n`. Otherwise, if `total_sum` is zero, either the index of the first non-zero element in `A` is found and the printed output is 'YES', '2', '1 i+1', 'i+2 n', or if no such element exists, the printed output is 'NO'.
#Overall this is what the function does:The function processes a list `A` of integers where the length of the list `n` satisfies 1 ≤ n ≤ 100, and each integer `a_i` in the list satisfies -10^3 ≤ a_i ≤ 10^3. After executing the function, the following states are possible:

1. If the sum of all elements in `A` is not zero, the function prints 'YES', '1', '1', and `n`. Here, 'YES' indicates that there is a way to partition the list into two parts with non-zero sums. '1' is the number of partitions, and the second '1' and `n` represent the start and end indices of the first partition.
   
2. If the sum of all elements in `A` is zero, the function searches for the first non-zero element in the list. If found, it prints 'YES', '2', '1', and `i+1`, followed by 'i+2' and `n`. Here, 'YES' indicates that there is a way to partition the list into two parts, '2' is the number of partitions, '1' and `i+1` represent the start and end indices of the first partition, and 'i+2' and `n` represent the start and end indices of the second partition. If no non-zero element is found, the function prints 'NO', indicating that it is not possible to partition the list into two parts with non-zero sums.


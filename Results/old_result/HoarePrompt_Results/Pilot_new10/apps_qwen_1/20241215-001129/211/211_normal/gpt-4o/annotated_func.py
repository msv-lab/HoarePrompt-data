#State of the program right berfore the function call: The input consists of two lines. The first line contains a single integer n (1 ≤ n ≤ 100) representing the number of elements in the array A. The second line contains n integers a_1, a_2, ..., a_n (-10^3 ≤ a_i ≤ 10^3) representing the elements of the array A.
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
            
        #State of the program after the  for loop has been executed: `n` is the integer value entered by the user, `A` is a list of `n` integers, `total_sum` is the sum of all elements in `A` and must be 0, `i` is `n`, and if any element in `A` is not 0, the loop breaks and prints 'YES', '2', '1', and the index + 1, followed by the index + 2 and `n`. If no element in `A` is not 0, the loop does not execute and prints 'NO'.
    #State of the program after the if-else block has been executed: `n` is the integer value entered by the user, `A` is a list of `n` integers, and `total_sum` is the sum of all elements in `A`. If `total_sum` is not equal to 0, the function does not change any variables and continues the execution with the updated state. If `total_sum` is 0, the function checks each element in `A`. If any element is not 0, it prints 'YES', '2', '1', the index (index + 1), followed by the index + 2 and `n`, and stops. If all elements are 0, it prints 'NO' and continues the execution with the updated state.
#Overall this is what the function does:The function reads an integer `n` followed by `n` integers to form an array `A`. It then calculates the sum of all elements in `A`. If the sum is not zero, it prints "YES", "1", "1", and "n". If the sum is zero, it checks each element in `A`. If any element is not zero, it prints "YES", "2", "1", the index (index + 1), followed by the index + 2 and `n`, and breaks the loop. If all elements are zero, it prints "NO".


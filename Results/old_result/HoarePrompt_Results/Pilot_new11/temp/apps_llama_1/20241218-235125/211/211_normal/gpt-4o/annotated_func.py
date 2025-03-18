#State of the program right berfore the function call: The input is a list of integers where the first element represents the number of elements in the array A, and the remaining elements represent the array A itself, where -10^3 ≤ a_i ≤ 10^3 and 1 ≤ n ≤ 100.
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
            
        #State of the program after the  for loop has been executed: 
    #State of the program after the if-else block has been executed: The list `A` is assigned the input list where `A[0]` is an integer `n` with 1 ≤ `n` ≤ 100, and -10^3 ≤ `A[i]` ≤ 10^3 for 1 ≤ `i` < `len(A)`, the input list has at least one element. If `total_sum` is not equal to 0, 'YES' has been printed, '1' has been printed twice, and the string '1' along with the value of `n` which is `A[0]` has been printed. If `total_sum` is equal to 0, no additional actions have been taken beyond the initial state described in the precondition.
#Overall this is what the function does:The function takes a list of integers as input where the first element represents the number of elements in the array, reads the input from the user, and processes the array to check if its elements sum up to zero or not. If the sum is not zero, it prints 'YES', '1', and the range '1' to 'n' (the length of the array). If the sum is zero, it iterates through the array to find the first non-zero element, prints 'YES', '2', the range '1' to the index of the non-zero element, and the range from the index after the non-zero element to 'n'. If all elements are zero, it does not print any additional output beyond the initial 'YES' and '2' for the case when a non-zero element is found, implying that no suitable range is found to print. The function modifies the state of the program by printing these outputs based on the input array's properties, but it does not return any value. It only prints the results based on the sum and elements of the array A.


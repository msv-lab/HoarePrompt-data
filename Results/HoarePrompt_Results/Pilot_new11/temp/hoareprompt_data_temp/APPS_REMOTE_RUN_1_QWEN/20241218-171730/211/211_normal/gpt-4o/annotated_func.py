#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 100, and the following list of integers represents the array A with length n, where each element a_i satisfies -10^3 ≤ a_{i} ≤ 10^3.
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
            
        #State of the program after the  for loop has been executed: `n` is an integer such that \(1 \leq n \leq 100\), `total_sum` is 0, and the console outputs 'NO'.
    #State of the program after the if-else block has been executed: *`n` is an integer such that 1 ≤ n ≤ 100; `A` contains `n` integers where each element `a_{i}` satisfies -10^3 ≤ a_{i} ≤ 10^3; `total_sum` is the sum of all elements in `A`; if `total_sum` is not equal to 0, the console outputs '1' followed by the value of `n`; if `total_sum` is 0, the console outputs 'NO'.
#Overall this is what the function does:The function processes an array \(A\) of length \(n\) (where \(1 \leq n \leq 100\)) with elements satisfying \(-10^3 \leq a_{i} \leq 10^3\). It checks if the sum of the elements in the array is zero. If the sum is non-zero, it prints 'YES' followed by '1' and the value of \(n\). If the sum is zero, it iterates through the array to find the first non-zero element and prints 'YES' followed by '2', then the indices of two segments that together cover the non-zero element (i.e., '1' and the index of the non-zero element, and the index of the non-zero element plus one and 'n'). If no non-zero element is found, it prints 'NO'.


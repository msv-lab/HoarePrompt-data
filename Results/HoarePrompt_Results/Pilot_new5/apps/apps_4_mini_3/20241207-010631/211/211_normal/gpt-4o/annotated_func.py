#State of the program right berfore the function call: n is a positive integer (1 ≤ n ≤ 100) representing the number of elements in array A, and A is a list of n integers where each integer a_i satisfies -10^3 ≤ a_i ≤ 10^3.
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
            
        #State of the program after the  for loop has been executed: `n` is an integer (1 ≤ n ≤ 100), `A` is a list of `n` integers, `total_sum` is equal to 0. If at least one element of `A` is not 0, then 'YES' has been printed, followed by '2', '1', and the index of the non-zero element plus one, along with the range from the next index to `n`. If all elements of `A` are 0, then 'NO' has been printed.
    #State of the program after the if-else block has been executed: *`n` is an input integer (1 ≤ `n` ≤ 100), `A` is a list of `n` integers where each integer `a_i` satisfies -10^3 ≤ `a_i` ≤ 10^3, and `total_sum` is equal to `sum(A)`. If `total_sum` is not equal to 0, the output is '1' followed by the value of `n`. If `total_sum` is equal to 0 and at least one element of `A` is not 0, 'YES' is printed followed by '2', '1', and the index of the non-zero element plus one, along with the range from the next index to `n`. If all elements of `A` are 0, 'NO' is printed.
#Overall this is what the function does:The function reads an integer `n` and a list of `n` integers `A`. If the sum of the integers in `A` is not zero, it prints 'YES', '1', and '1 n'. If the sum is zero and there is at least one non-zero element in `A`, it prints 'YES', '2', '1', and the index of the first non-zero element plus one, followed by the range from the next index to `n'. If all elements of `A` are zero, it prints 'NO'.


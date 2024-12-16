#State of the program right berfore the function call: The input consists of an integer n (1 ≤ n ≤ 100), followed by a list of n integers a_1, a_2,..., a_{n} ( - 10^3 ≤ a_{i} ≤ 10^3), representing the elements of array A.
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
            
        #State of the program after the  for loop has been executed: `n` is an integer between 1 and 100 (inclusive), `A` is a list of `n` integers each in the range -10^3 to 10^3, `total_sum` equals 0, `i` is either `n` if all elements in `A` are 0 or the index of the first non-zero element in `A`, and either 'YES', '2', and specific indices have been printed if a non-zero element was found, or 'NO' has been printed if all elements are 0.
    #State of the program after the if-else block has been executed: `n` is an integer between 1 and 100 (inclusive), `A` is a list of `n` integers each in the range -10^3 to 10^3, `total_sum` equals the sum of all elements in `A`, ranging from `-10^5` to `10^5`. If `total_sum` is not equal to 0, 'YES' has been printed, '1' has been printed twice, and `n` has been printed. If `total_sum` equals 0, then either 'NO' has been printed if all elements in `A` are 0, or 'YES', '2', and specific indices have been printed if a non-zero element was found in `A`.
#Overall this is what the function does:The function accepts an integer n and a list of n integers, calculates the sum of the integers, and prints 'YES' along with specific information based on whether the sum is non-zero or if a non-zero element is found in the list; if all elements are 0, it does not print anything.


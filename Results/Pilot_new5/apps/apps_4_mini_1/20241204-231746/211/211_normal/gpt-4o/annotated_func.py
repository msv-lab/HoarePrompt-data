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
            
        #State of the program after the  for loop has been executed: `n` is a positive integer between 1 and 100, `A` is a list of `n` integers within the range -1000 ≤ `a_i` ≤ 1000, `total_sum` is 0. If there is at least one non-zero element in `A`, 'YES' is printed along with '2', followed by two indices indicating the position of that non-zero element and the end of the list; otherwise, 'NO' is printed if all elements are zero.
    #State of the program after the if-else block has been executed: *`n` is a positive integer such that 1 ≤ `n` ≤ 100, `A` is a list of `n` integers each satisfying -1000 ≤ `a_i` ≤ 1000, and `total_sum` is the sum of elements in `A`. If `total_sum` is not equal to 0, '1' is printed along with the value of `n`. If `total_sum` is 0 and there is at least one non-zero element in `A`, 'YES' is printed along with '2', followed by two indices indicating the position of that non-zero element and the end of the list; otherwise, 'NO' is printed if all elements are zero.
#Overall this is what the function does:The function accepts an integer `n` (1 ≤ n ≤ 100) and a list `A` of `n` integers, where each integer satisfies -1000 ≤ a_i ≤ 1000. It calculates the sum of the elements in `A`. If the sum is not zero, it prints 'YES', followed by '1' and the value of `n`. If the sum is zero but at least one element in `A` is non-zero, it prints 'YES', followed by '2' and the indices of the first non-zero element and the end of the list. If all elements are zero, it prints 'NO'. The function does not return any values; it only prints output based on the conditions.


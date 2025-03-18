#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 1 ≤ n ≤ 3 \cdot 10^5, and the array a is a list of n integers where 1 ≤ a_i ≤ n. The array a is guaranteed to be beautiful, and the sum of n over all test cases does not exceed 3 \cdot 10^5.
def func_1():
    n = int(input())
    arr = list(map(int, input().split()))
    flag = True
    for i in range(1, n):
        if arr[i] != arr[i - 1]:
            flag = False
            break
        
    #State: Postcondition: `flag` remains `False`, `i` is equal to `n`, `n` is an input integer greater than 4, `arr` is a list of integers obtained from splitting the input and converting each element to an integer, and the loop has executed for all values of `i` from 1 to `n-1`. If `arr[i]` is not equal to `arr[i - 1]` for any `i`, the loop breaks out of the iteration early due to the `break` statement.
    ans = Decimal('Infinity')
    val, cnt = arr[0], 0
    for i in range(n):
        if arr[i] == val:
            cnt += 1
        else:
            ans = min(ans, cnt)
        
    #State: All elements of `arr` have been iterated over, `i` is equal to `n`, `ans` is the minimum count of consecutive occurrences of `val` in `arr` plus one for any segment that does not start with `val`.
    ans = min(ans, cnt)
    if flag :
        print(-1)
        #This is printed: -1
    else :
        print(ans)
        #This is printed: ans (where ans is the minimum count of consecutive occurrences of val in arr plus one for any segment that does not start with val)
    #State: Postcondition: `ans` is the minimum count of consecutive occurrences of `val` in `arr` plus one for any segment that does not start with `val`, and `cnt` is updated to be the new value of `ans`. This holds whether the `flag` is true or false.
#Overall this is what the function does:The function processes a set of test cases, each consisting of an integer \( n \) and a list of \( n \) integers \( a \). It checks if the list \( a \) is monotonically the same (i.e., all elements are identical). If the list is not monotonically the same, it finds the minimum count of consecutive occurrences of any element in the list, excluding the first element of the segment. The function then prints either \(-1\) if the list is monotonically the same or the calculated minimum count otherwise.


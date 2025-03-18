#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 1 ≤ n ≤ 3 \cdot 10^5, and the array a is a list of n integers where 1 ≤ a_i ≤ n. The array a is guaranteed to be beautiful, and the sum of n over all test cases does not exceed 3 \cdot 10^5.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        ar = list(map(int, input().split()))
        
        same = 1
        
        num = ar[0]
        
        minn = inf
        
        i = 1
        
        while i < len(ar):
            if ar[i] == num:
                same += 1
            else:
                i += 1
                num = ar[i]
                minn = min(minn, same)
                same = 1
            i += 1
        
        minn = min(minn, same)
        
        if minn == inf:
            print(-1)
        else:
            print(minn)
        
    #State: After all iterations of the loop, `minn` will hold the minimum count of consecutive occurrences of any number in the entire list `ar`. `same` will be 1 because the loop has finished, meaning no new consecutive sequence is being counted. `num` will be the last element of the list `ar` that was processed. `i` will be equal to `len(ar)`. `t` will be an integer such that \(1 \leq t \leq 10^4\), `n` will be the last input integer, and `minn` will be the smallest value among all the counts of consecutive occurrences of any number in all lists `ar` across all test cases.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `n` and a list of `n` integers `ar`. It determines the minimum count of consecutive occurrences of any number in the list `ar` across all test cases. If no such occurrence exists, it prints -1; otherwise, it prints the minimum count. The function does not return any value but prints the result for each test case.


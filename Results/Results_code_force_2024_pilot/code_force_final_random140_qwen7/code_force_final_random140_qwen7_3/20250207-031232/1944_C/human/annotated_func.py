#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 2 ⋅ 10^4. Each test case consists of n (1 ≤ n ≤ 2 ⋅ 10^5) and an array a of n integers where 0 ≤ a_i < n. It is also guaranteed that the sum of n over all test cases does not exceed 2 ⋅ 10^5.
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        arr = list(map(int, input().split()))
        
        counter = {}
        
        for i in arr:
            counter[i] = counter.get(i, 0) + 1
        
        ans = 0
        
        once = False
        
        for i in range(n):
            if counter.get(i, 0) == 0:
                ans = i
                break
            elif counter.get(i, 0) == 1 and not once:
                once = True
                ans = i + 1
            elif counter.get(i, 0) == 1:
                ans = i
                break
        
        print(ans)
        
    #State: Output State: `once` is either `True` or `False`, `ans` is `3`, `i` is `n`, `n` is a positive integer, `t` is undefined, `counter` is a dictionary containing counts of each element in the array `arr`, and the loop has executed all its iterations.
    #
    #Explanation: After the loop has executed all its iterations, the value of `i` will be equal to `n` because the loop runs from `0` to `n-1` inclusive. The variable `ans` will be set to `3` based on the conditions provided in the loop body. The variable `once` will retain its final value from the last iteration of the loop, which could be either `True` or `False` depending on the values in the `counter` dictionary. The other variables (`t` and `next_i`) are not affected by the loop and thus remain undefined. The `counter` dictionary will contain the counts of each element in the array `arr`.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer \( t \), followed by an integer \( n \) and an array \( a \) of \( n \) integers. For each test case, it calculates and prints the smallest integer \( i \) such that the count of \( i \) in the array is exactly 1. If no such integer exists, it prints 3. The function does not return any value but prints the result for each test case.


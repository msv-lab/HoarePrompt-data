#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 100. For each test case, n and m are integers satisfying 1 ≤ n ≤ m ≤ 2 ⋅ 10^5, and the sum of m over all test cases does not exceed 2 ⋅ 10^5. a_i and b_i are integers such that 1 ≤ a_i, b_i ≤ 10^9 for all i.
def func():
    for _ in range(int(input())):
        n, m = map(int, input().split())
        
        a = list(map(int, input().split()))
        
        c = list(map(int, input().split()))
        
        if len(set(a)) == 1 and len(set(c)) == 1 and a[0] == c[0]:
            print(0)
            continue
        
        a.sort()
        
        c.sort(reverse=True)
        
        if len(a) == 1:
            print(max(abs(a[0] - max(c)), abs(a[0] - min(c))))
            continue
        
        i, j, ans = 0, 1, 0
        
        for k in range(len(a)):
            t1 = abs(a[i] - c[i])
            t2 = abs(a[len(a) - j] - c[len(c) - j])
            if t2 > t1:
                j += 1
            else:
                i += 1
            ans += max(t1, t2)
        
        print(ans)
        
    #State: Output State: The output state will consist of a series of integers printed as the result of the loop's execution for each test case. Each integer represents the calculated value of `ans` for that specific test case based on the given conditions and operations within the loop. If the conditions inside the if statement are met, the loop will print 0 and skip further calculations for that test case. Otherwise, it will sort lists `a` and `c`, initialize pointers `i` and `j`, and compute the value of `ans` by iterating through the sorted lists, comparing elements, and accumulating the maximum absolute differences.
#Overall this is what the function does:The function processes multiple test cases, each involving integers n and m, along with two lists a and c. It first checks if the values in lists a and c are identical and constant across all elements. If so, it prints 0 and skips further processing. Otherwise, it sorts lists a in ascending order and c in descending order. Then, it calculates the sum of the maximum absolute differences between corresponding elements of the sorted lists a and c, printing the total sum for each test case.


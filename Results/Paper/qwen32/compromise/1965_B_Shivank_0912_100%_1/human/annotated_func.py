#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000. Each test case consists of two integers n and k such that 2 ≤ n ≤ 10^6 and 1 ≤ k ≤ n. The sum of n over all test cases does not exceed 10^7.
def func():
    t = int(input())
    for tc in range(t):
        n, k = map(int, input().split())
        
        i = 0
        
        while 1 << i + 1 <= k:
            i = i + 1
        
        ans = [k - (1 << i), k + 1, k + 1 + (1 << i)]
        
        for j in range(20):
            if j != i:
                ans.append(1 << j)
        
        print(len(ans))
        
        print(*ans)
        
    #State: For each test case, the output consists of the length of the list `ans` followed by the elements of the list `ans`, where `ans` is constructed as described above for each test case.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads two integers `n` and `k`. It then constructs a list `ans` based on the value of `k` and prints the length of this list followed by its elements.


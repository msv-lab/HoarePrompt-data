#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 1000, and for each test case, n and k are positive integers satisfying 2 <= n <= 10^6 and 1 <= k <= n. Additionally, the sum of all n values across all test cases does not exceed 10^7.
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
        
    #State: The list `ans` will contain all integers from 1 to 20, excluding the value at index `i` if `i` is less than 20.
#Overall this is what the function does:The function processes multiple test cases, each consisting of three integers: t (the number of test cases), n (the size of the set), and k (an integer within the set). For each test case, it calculates a list of integers and prints the length of this list followed by the list itself. The list contains all integers from 1 to 20, excluding the integer at index `i`, where `i` is determined based on the value of `k`.


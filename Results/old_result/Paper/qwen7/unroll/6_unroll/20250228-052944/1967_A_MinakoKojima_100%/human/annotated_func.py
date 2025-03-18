#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100. For each test case, n and k are integers such that 1 ≤ n ≤ 2 \cdot 10^5 and 0 ≤ k ≤ 10^{12}. The list a contains n integers such that 1 ≤ a_i ≤ 10^{12}, representing the number of cards of type i initially.
def func():
    ans_list = []
    for _ in range(int(input())):
        n, k = map(int, input().split())
        
        a = list(map(int, input().split()))
        
        a.sort()
        
        ans = a[0]
        
        res = n - 1
        
        for i in range(n - 1):
            dif = a[i + 1] - a[i]
            if dif == 0:
                res -= 1
            if dif != 0:
                if k >= dif * (i + 1):
                    ans += dif
                    k -= dif * (i + 1)
                    res -= 1
                else:
                    ans += k // (i + 1)
                    if i != 0:
                        res += k % (i + 1)
                    k = 0
                    break
                if k == 0:
                    break
        
        if k != 0:
            ans += k // n
            res += k % n
        
        ans += (ans - 1) * (n - 1)
        
        ans += res
        
        ans_list.append(ans)
        
    #State: Output State: `ans_list` is a list containing integers where each integer is calculated based on the given logic within the loop for each set of inputs provided. The exact values in the list depend on the inputs provided during the execution of the loop.
    for a in ans_list:
        print(a)
        
    #State: The output state will be a list of integers printed for each element in `ans_list`. Each integer printed corresponds to the value of `a` in the loop for each iteration.
#Overall this is what the function does:The function processes multiple test cases, each consisting of integers \( n \), \( k \), and a list \( a \) of \( n \) integers. For each test case, it calculates a value based on the given logic involving sorting the list \( a \), adjusting the value of \( ans \) based on differences between consecutive elements in \( a \) and the integer \( k \). After processing all test cases, it prints the calculated values for each test case.


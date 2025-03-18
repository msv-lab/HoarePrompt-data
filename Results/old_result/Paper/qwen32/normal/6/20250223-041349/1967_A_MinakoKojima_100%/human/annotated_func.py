#State of the program right berfore the function call: Each test case consists of two integers n (1 ≤ n ≤ 2 · 10^5) and k (0 ≤ k ≤ 10^12), followed by a list of n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 10^12), representing the number of cards of each type initially. The number of test cases t (1 ≤ t ≤ 100) is provided at the beginning, and the sum of n over all test cases does not exceed 5 · 10^5.
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
        
    #State: ans_list contains the final calculated `ans` values for each test case.
    for a in ans_list:
        print(a)
        
    #State: the loop will print each element in `ans_list` until all elements are printed.
#Overall this is what the function does:The function processes multiple test cases, each consisting of two integers `n` and `k`, and a list of `n` integers representing the number of cards of each type. For each test case, it computes a value based on the given inputs and prints the result. The computation involves sorting the list of card counts, adjusting the counts based on the value of `k`, and then calculating a final value that includes adjustments for the remaining `k` and the differences in card counts.


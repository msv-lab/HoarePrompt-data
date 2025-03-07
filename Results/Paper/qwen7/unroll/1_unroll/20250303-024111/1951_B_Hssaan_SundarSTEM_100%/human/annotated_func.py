#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n and k are integers such that 2 ≤ n ≤ 10^5 and 1 ≤ k ≤ n. Additionally, a list a of n integers is given such that 1 ≤ a_i ≤ 10^9 and all a_i's are pairwise different.
def func():
    for _ in range(int(input())):
        n, k = list(map(int, input().split()))
        
        s = list(map(int, input().split()))
        
        s[0], s[k - 1] = s[k - 1], s[0]
        
        ans = 0
        
        h = s[0]
        
        j = -1
        
        for i in s[1:]:
            j += 1
            if h < i:
                break
            else:
                ans += 1
        
        p = j + 1
        
        s[0], s[k - 1] = s[k - 1], s[0]
        
        ans1 = 0
        
        s[p], s[k - 1] = s[k - 1], s[p]
        
        z = 0
        
        for i in s:
            if i == h:
                if s[0] != h:
                    ans1 += 1
                z = 1
            elif i > h:
                break
            elif z == 1:
                ans1 += 1
        
        print(max(ans, ans1))
        
    #State: Output State: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n and k are integers such that 2 ≤ n ≤ 10^5 and 1 ≤ k ≤ n. Additionally, a list a of n integers is given such that 1 ≤ a_i ≤ 10^9 and all a_i's are pairwise different. After executing the loop, the value of `ans` is determined by comparing the first element of the list `s` with the elements following it up to index `k-1`, and counting how many elements are greater than or equal to the first element. The value of `ans1` is determined by finding the first occurrence of the maximum element (initially stored in `h`) in the list starting from index `p+1` to `k-1`, and counting how many elements are greater than or equal to this maximum element. The final output is the maximum of `ans` and `ans1`.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `n`, an integer `k`, and a list of `n` unique integers. For each test case, it swaps the first element of the list with the element at index `k-1`, then counts how many elements in the sublist starting from the first element up to index `k-1` are greater than or equal to the first element. It then swaps back the first and the element at index `k-1`. Next, it finds the first occurrence of the maximum element in the list starting from the element at index `p+1` to `k-1`, and counts how many elements in this sublist are greater than or equal to this maximum element. Finally, it prints the maximum of the two counts obtained.


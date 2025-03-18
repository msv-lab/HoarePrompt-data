#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4; for each test case, n and k are integers such that 2 ≤ n ≤ 10^5 and 1 ≤ k ≤ n; a is a list of n integers such that 1 ≤ a_i ≤ 10^9 and all a_i's are distinct.
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
        
    #State: Output State: t is an integer such that 1 ≤ t ≤ 10^4; for each test case, n and k are integers such that 2 ≤ n ≤ 10^5 and 1 ≤ k ≤ n; a is a list of n integers such that 1 ≤ a_i ≤ 10^9 and all a_i's are distinct; after executing the loop, ans and ans1 are integers representing the results of the comparisons within the loop, and the list s is modified according to the operations performed within the loop.
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it reads the values of \( n \) and \( k \), and a list \( s \) of \( n \) distinct integers. It then swaps the first element of \( s \) with the element at index \( k-1 \). After this swap, it counts the number of elements in \( s \) that are greater than or equal to the first element and stores this count in \( ans \). Next, it swaps the element at index \( p \) (where \( p \) is the position found during the first count) with the element at index \( k-1 \) again, and counts the number of elements in \( s \) that are greater than or equal to the first element after this second swap and stores this count in \( ans1 \). Finally, it prints the maximum value between \( ans \) and \( ans1 \).


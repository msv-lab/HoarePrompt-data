#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 2 ⋅ 10^4. For each test case, n is a positive integer such that 1 ≤ n ≤ 2 ⋅ 10^5, and a is a list of n non-negative integers where each integer a_i satisfies 0 ≤ a_i < n. The sum of all n values across all test cases does not exceed 2 ⋅ 10^5.
def func():
    for tc in range(int(input())):
        N = int(input())
        
        a = list(map(int, input().split()))
        
        cnt = defaultdict(int)
        
        for i in range(N):
            cnt[a[i]] += 1
        
        t = 0
        
        for i in range(N):
            if cnt[i] == 1:
                t += 1
            if t >= 2 or cnt[i] == 0:
                print(i)
                break
        
    #State: Output State: t is a positive integer such that 1 ≤ t ≤ 2 ⋅ 10^4. For each test case, N is a positive integer such that 1 ≤ N ≤ 2 ⋅ 10^5, and a is a list of N non-negative integers where each integer a_i satisfies 0 ≤ a_i < N. The value of t is incremented for each unique element in the list a until either two unique elements are found or a zero is encountered. If two unique elements are found or a zero is encountered, the index of the first unique element is printed and the loop breaks. The output state describes the indices of the first unique elements for each test case or the first zero encountered, whichever comes first.
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it reads an integer \(N\) and a list of \(N\) non-negative integers \(a\). It then counts the occurrences of each integer in the list. The function increments a counter \(t\) for each unique integer until it finds either two unique integers or encounters a zero. If two unique integers are found or a zero is encountered, it prints the index of the first unique integer and stops processing further integers in the current test case. The function does not return any value but prints the index of the first unique integer or the first zero for each test case.


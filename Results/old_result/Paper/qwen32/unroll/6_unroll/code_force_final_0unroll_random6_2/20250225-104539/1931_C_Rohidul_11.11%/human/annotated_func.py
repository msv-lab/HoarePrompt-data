#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 1 ≤ n ≤ 2 · 10^5, and a is a list of n integers where each integer a_i satisfies 1 ≤ a_i ≤ n. The sum of n over all test cases does not exceed 2 · 10^5.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        l, r = 0, n - 1
        
        st, end = 0, 0
        
        while l < r and a[l] == a[l + 1]:
            l += 1
            st += 1
        
        while r > l and a[r] == a[r - 1]:
            r -= 1
            end += 1
        
        if a[0] == a[-1]:
            ans = r - l - 1
        elif st == 0 and end == 0 and a[0] != a[-1]:
            ans = len(a) - 1
        else:
            ans = r - l
        
        print(max(0, ans))
        
    #State: The output state consists of t lines, each representing the result of the corresponding test case. For each test case, the output is the maximum number of elements that can be removed from the list a such that the first and last elements of the remaining list are not the same consecutive elements. The value of t, n, and the list a remain unchanged from the initial state.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a list of integers. For each test case, it calculates and prints the maximum number of elements that can be removed from the list such that the first and last elements of the remaining list are not the same consecutive elements. The input values for the number of test cases, the size of each list, and the list elements themselves remain unchanged after the function executes.


#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 1000. Each test case consists of three integers n, f, and k such that 1 <= f, k <= n <= 100, and a list of n integers a_i where 1 <= a_i <= 100.
def func():
    t = int(input())
    for _ in range(t):
        n, f, k = map(int, input().split())
        
        a = list(map(int, input().split()))
        
        favorite_value = a[f - 1]
        
        sorted_a = sorted(a, reverse=True)
        
        removed_count = 0
        
        for i in range(k):
            if sorted_a[i] == favorite_value:
                removed_count += 1
        
        favorite_count = sorted_a.count(favorite_value)
        
        if removed_count == favorite_count:
            print('YES')
        elif removed_count == 0:
            print('NO')
        else:
            print('MAYBE')
        
    #State: Output State: The output state will consist of 'YES', 'NO', or 'MAYBE' printed for each iteration of the loop based on the conditions specified in the loop body. For each iteration, if the count of the favorite value being removed matches the total count of the favorite value in the sorted list, it prints 'YES'. If the favorite value is never removed, it prints 'NO'. Otherwise, it prints 'MAYBE'.
#Overall this is what the function does:The function processes multiple test cases, each consisting of three integers \( n \), \( f \), and \( k \), and a list of \( n \) integers \( a_i \). For each test case, it determines whether the favorite value (the \( f \)-th element in the list) is removed exactly as many times as it appears in the list when the list is sorted in descending order. Based on this comparison, it outputs either 'YES', 'NO', or 'MAYBE' for each test case.


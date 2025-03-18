#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000. For each test case, n, f, and k are integers such that 1 <= f, k <= n <= 100, and a is a list of n integers where each element a_i satisfies 1 <= a_i <= 100.
def func():
    t = int(input())
    for _ in range(t):
        n, f, k = map(int, input().split())
        
        a = list(map(int, input().split()))
        
        favorite_value = a[f - 1]
        
        same_value_count = 0
        
        for value in a:
            if value == favorite_value:
                same_value_count += 1
        
        greater_count = 0
        
        for value in a:
            if value > favorite_value:
                greater_count += 1
        
        if greater_count >= k:
            print('YES')
        elif greater_count + same_value_count <= k:
            print('NO')
        else:
            print('MAYBE')
        
    #State: The variables `n`, `f`, `k`, and `a` will reflect the values from the last iteration, and the output will be 'YES', 'NO', or 'MAYBE' based on the conditions evaluated in the last iteration.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a list of integers and additional parameters. For each test case, it determines if the number of elements greater than a specified favorite element, plus the favorite element itself if necessary, meets or exceeds a given threshold. It outputs 'YES' if the threshold is met, 'NO' if it is not possible to meet the threshold, and 'MAYBE' if it might be possible depending on the distribution of elements.


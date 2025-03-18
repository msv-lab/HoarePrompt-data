#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 2⋅10^4. Each test case consists of n (1 ≤ n ≤ 2⋅10^5) integers a_1, a_2, ..., a_n where 0 ≤ a_i < n. The sum of all n across all test cases does not exceed 2⋅10^5.
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        arr = list(map(int, input().split()))
        
        counter = {}
        
        for i in arr:
            counter[i] = counter.get(i, 0) + 1
        
        ans = 0
        
        once = False
        
        for i in range(n):
            if counter.get(i, 0) == 0:
                ans = i
                break
            elif counter.get(i, 0) == 1 and not once:
                once = True
                ans = i + 1
            elif counter.get(i, 0) == 1:
                ans = i
                break
        
        print(ans)
        
    #State: The loop has executed all iterations, meaning `i` is now equal to `n-1`. The value of `ans` will be the highest unique element in `arr` plus one if such an element exists, otherwise it will be the highest unique element. The variable `once` will be True if at least one element with a frequency of 1 was found before encountering an element with a frequency of 0. The variable `i` will be set to the last index of `arr`, and `n` will remain as the length of `arr`. The `counter` dictionary will reflect the frequency of each element in the array `arr`.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer \( n \) followed by \( n \) integers. For each test case, it calculates the highest unique integer in the array and adds one to it if such an integer exists; otherwise, it outputs the highest unique integer. The function prints the result for each test case.


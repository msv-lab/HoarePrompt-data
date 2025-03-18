#State of the program right berfore the function call: The input consists of multiple test cases. Each test case starts with two integers n and m (1 ≤ n ≤ m ≤ 2 · 10^5), followed by n integers a_i (1 ≤ a_i ≤ 10^9) representing Petya's array, and m integers b_i (1 ≤ b_i ≤ 10^9) representing the integers Vasya can choose from. The total number of integers m across all test cases does not exceed 2 · 10^5.
def func():
    for _ in range(int(input())):
        n, m = map(int, input().split())
        
        temp = -1
        
        ans = []
        
        a = sorted(map(int, input().split()))[:n]
        
        b = sorted(map(int, input().split()), reverse=True)[:m]
        
        for i in range(n):
            if abs(a[i] - b[-(n - i)]) > abs(a[i] - b[i]):
                temp = i
                break
            ans.append(abs(a[i] - b[i]))
        
        if temp != -1:
            for i in range(temp, n):
                ans.append(abs(a[i] - b[-(n - i)]))
        
        print(sum(ans))
        
    #State: The output state after the loop executes all the iterations is the sum of the absolute differences between the elements of the sorted array `a` and the elements of the sorted array `b` (in reverse order), calculated according to the specified conditions.
#Overall this is what the function does:The function processes multiple test cases, where each test case involves two arrays: Petya's array `a` of length `n` and Vasya's array `b` of length `m`. It calculates and prints the sum of the absolute differences between elements of the sorted Petya's array and a selected subset of Vasya's array. The selection from Vasya's array is done in a specific manner based on the comparison of absolute differences, ensuring the minimum possible sum for the given conditions.


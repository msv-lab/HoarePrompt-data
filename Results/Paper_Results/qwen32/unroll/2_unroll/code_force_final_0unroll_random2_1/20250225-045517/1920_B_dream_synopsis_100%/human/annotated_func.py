#State of the program right berfore the function call: Each test case consists of three integers n, k, and x (1 ≤ n ≤ 2 · 10^5, 1 ≤ k, x ≤ n) representing the number of elements in the array, the limit on the number of elements Alice can remove, and the limit on the number of elements Bob can multiply by -1, respectively. The second line of each test case contains n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 1000) representing the elements of the array. The total number of elements across all test cases does not exceed 2 · 10^5.
def func():
    for _ in range(int(input())):
        n, k, x = map(int, input().split())
        
        a = list(map(int, input().split()))
        
        a.sort()
        
        a.reverse()
        
        sum1 = sum(a)
        
        ans = []
        
        for i in range(k + 1):
            if i == 0:
                sums = sum1 - 2 * sum(a[:x])
                ans.append(sums)
            elif i + x - 1 < n:
                sums = sums + a[i - 1] - 2 * a[i + x - 1]
                ans.append(sums)
            else:
                sums = sums + a[i - 1]
                ans.append(sums)
        
        print(max(ans))
        
    #State: maximum_sum
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer array and two limits `k` and `x`. For each test case, it calculates the maximum possible sum of the array after removing up to `k` elements and multiplying up to `x` elements by -1. The function outputs the maximum sum for each test case.


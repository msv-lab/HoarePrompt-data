#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 2 ⋅ 10^4. Each test case consists of n (1 ≤ n ≤ 2 ⋅ 10^5) and an array a of n integers where 0 ≤ a_i < n. The sum of all n values across all test cases does not exceed 2 ⋅ 10^5.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        arr = list(map(int, input().split()))
        
        mpp = Counter(arr)
        
        first = False
        
        for i in range(n):
            if i not in mpp.keys():
                print(i)
                break
            if mpp[i] == 1 and first:
                print(i)
                break
            if mpp[i] == 1:
                first = True
        
    #State: Output State: t is a positive integer such that 1 ≤ t ≤ 2 ⋅ 10^4. Each test case consists of n (1 ≤ n ≤ 2 ⋅ 10^5) and an array a of n integers where 0 ≤ a_i < n. The sum of all n values across all test cases does not exceed 2 ⋅ 10^5. After executing the loop, for each test case, if there is an index i that does not appear in the array, it prints i and breaks. If there is exactly one occurrence of each index from 0 to i-1 and i has already appeared once before, it prints i and breaks. Otherwise, it continues to the next index.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer \( n \) and an array \( a \) of \( n \) integers. For each test case, it checks if there is an index \( i \) that does not appear in the array or if there is exactly one occurrence of each index from 0 to \( i-1 \) and the index \( i \) has already appeared once before. If either condition is met, it prints the index \( i \) and breaks. If no such index is found, it continues to the next index. The function does not return any value but outputs the results for each test case.


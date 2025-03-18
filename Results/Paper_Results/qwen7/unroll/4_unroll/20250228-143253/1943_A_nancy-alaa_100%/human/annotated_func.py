#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 2 ⋅ 10^4. Each test case consists of n (1 ≤ n ≤ 2 ⋅ 10^5) and an array a of n integers where 0 ≤ a_i < n. It is also guaranteed that the sum of n over all test cases does not exceed 2 ⋅ 10^5.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        arr = list(map(int, input().split()))
        
        mpp = Counter(arr)
        
        first = False
        
        for i in range(n + 1):
            if i not in mpp.keys():
                print(i)
                break
            if mpp[i] == 1 and first:
                print(i)
                break
            if mpp[i] == 1:
                first = True
        
    #State: Output State: The output is the smallest missing index in the array `arr` or the smallest index that appears exactly once in `arr` after the first occurrence of such an index. If no such index exists, it outputs -1.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer \( n \) and an array \( a \) of \( n \) integers. For each test case, it finds and prints either the smallest missing index in the array or the smallest index that appears exactly once in the array after its first occurrence. If no such index exists, it prints -1.


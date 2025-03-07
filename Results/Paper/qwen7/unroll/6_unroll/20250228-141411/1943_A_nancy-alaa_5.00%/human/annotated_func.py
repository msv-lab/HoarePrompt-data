#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 2 ⋅ 10^4. For each test case, n is a positive integer such that 1 ≤ n ≤ 2 ⋅ 10^5, and a is a list of n non-negative integers where each integer a_i satisfies 0 ≤ a_i < n. The sum of all n values across all test cases does not exceed 2 ⋅ 10^5.
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
        
    #State: Output State: t is a positive integer such that 1 ≤ t ≤ 2 ⋅ 10^4. For each test case, n is a positive integer such that 1 ≤ n ≤ 2 ⋅ 10^5, and a is a list of n non-negative integers where each integer a_i satisfies 0 ≤ a_i < n. After executing the loop, for each test case, if there exists an index i that does not appear in the list a, it will be printed first. If no such index exists, the loop checks for indices with exactly one occurrence and prints the first one found after setting `first` to true. If no such index is found, no output is generated for that test case.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads a positive integer \( n \) and a list of \( n \) non-negative integers. It then determines if there is any index \( i \) (where \( 0 \leq i < n \)) that does not appear in the list. If such an index exists, it prints the index. Otherwise, it checks for indices that appear exactly once in the list and prints the first one found after setting a flag. If neither condition is met for a test case, no output is generated for that case.


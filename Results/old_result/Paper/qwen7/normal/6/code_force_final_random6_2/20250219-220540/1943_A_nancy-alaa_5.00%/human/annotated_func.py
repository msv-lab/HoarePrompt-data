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
        
    #State: Output State: The loop will continue to iterate for all test cases provided by the input. After all iterations, the value of `i` will be the smallest index that either does not exist in the array `arr` or exists but has a count of 1 in the counter `mpp`, and `first` will remain `True`. The variable `mpp` will be a Counter object containing the counts of each element in `arr` for the last test case processed. If such an `i` is found during any iteration, it will be printed and the loop will terminate early. If no such `i` is found, the loop will process all test cases, and the final value of `i` will be the length of the last `arr` list, assuming no earlier condition was met to break the loop.
    #
    #In simpler terms, after processing all test cases, `i` will be the smallest missing index or the first index with a single occurrence (if `first` becomes `True`), or the size of the last input list if no such index is found. The `mpp` will reflect the counts of elements in the last input list, and `first` will indicate if a unique element was found previously.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a positive integer \( n \) and a list of \( n \) non-negative integers. For each test case, it determines and prints the smallest index \( i \) that either does not exist in the list or exists but appears exactly once. If no such index is found, it prints the length of the list. The function uses a counter to keep track of the occurrences of each element in the list and iterates through the list to find the required index. The final output depends on the conditions met during the iteration.


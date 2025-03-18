#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 2⋅10^4. Each test case consists of n (1 ≤ n ≤ 2⋅10^5) and an array a of n integers where 0 ≤ a_i < n. It is also guaranteed that the sum of n over all test cases does not exceed 2⋅10^5.
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
        
    #State: Output State: The loop will continue to execute until it processes all test cases. After all iterations, `first` will either be True or False depending on whether a unique element (with a count of 1) was found after the first unique element. The value of `i` will be -1 because the loop breaks when it finds the required condition. `n` will be the last input integer processed, `arr` will be the last list of integers based on the final input, and `mpp` will be the `Counter` object containing the count of each element in `arr`. If no elements with a count of 1 were found after the first unique element, `first` will remain False; otherwise, it will be True.
    #
    #The loop will terminate once all test cases are processed, and the conditions specified in the loop body are no longer met for any remaining elements.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer \( n \) and an array \( a \) of \( n \) integers. For each test case, it prints the smallest missing integer or the smallest integer with a count of 1 after the first unique element. If no such element is found, it prints -1. The function does not return any value but prints the results for each test case.


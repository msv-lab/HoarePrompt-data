#State of the program right berfore the function call: t is a positive integer representing the number of test cases. For each test case, n is a positive integer representing the length of the array a, and a is a list of n integers where each integer is between 1 and 10^9 inclusive.
def func():
    """Median of Array"""
    t = int(input())
    for _ in range(t):
        n = int(input().strip())
        
        a = list(map(int, input().strip().split()))
        
        a.sort()
        
        p = (n + 1) // 2 - 1
        
        res = a[p:].count(a[p])
        
        print(res)
        
    #State: Output State: After the loop executes all the iterations, `t` must be a positive integer, representing the total number of test cases. For each test case, `n` is an input integer representing the length of the array `a`, and `a` is a list of `n` integers sorted in ascending order. The variable `p` is calculated as `(n + 1) // 2 - 1`, which represents the index of the middle element or the element just before the middle if `n` is even. The variable `res` is the count of the element at index `p` in the sublist `a[p:]` of the array `a`. This value of `res` will be printed for each test case after sorting the array `a` and performing the count operation.
    #
    #In summary, after all iterations of the loop, `t` test cases will have been processed, and for each case, the count of the middle element (or the element just before the middle if `n` is even) in the second half of the sorted array will be printed.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads the number of elements in the array and the array itself, sorts the array in ascending order, calculates the index of the middle element (or the element just before the middle if the array length is even), counts the occurrences of the middle element in the second half of the sorted array, and prints this count. After processing all test cases, the function does not return any value but ensures that for each test case, the count of the specified element is printed.


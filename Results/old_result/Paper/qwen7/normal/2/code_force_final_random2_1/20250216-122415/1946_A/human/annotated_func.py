#State of the program right berfore the function call: t is a positive integer representing the number of test cases. For each test case, n is a positive integer representing the length of the array a, and a is a list of n integers where each integer is in the range [1, 10^9].
def func():
    """Median of Array"""
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        a.sort()
        
        p = (n + 1) // 2 - 1
        
        res = a.count(a[p])
        
        print(res)
        
    #State: After the loop executes all the iterations, `t` will be 0, `n` is the last input integer, `a` is a sorted list of integers obtained from splitting the last input string and converting each element to an integer, `p` is `(n + 1) // 2 - 1`, and `res` is the count of elements in `a` that are equal to `a[p]`.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads the length of an array and the array itself, sorts the array, finds the middle element, counts how many times this middle element appears in the sorted array, and prints this count. After processing all test cases, the function does not return any value.


#State of the program right berfore the function call: The input consists of multiple test cases. Each test case starts with an integer n (2 ≤ n ≤ 100) representing the length of the array, followed by n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 10^9) representing the elements of the array. The first line of the input contains a single integer t (1 ≤ t ≤ 500) indicating the number of test cases.
def func():
    ntest = int(input())
    for itest in range(0, ntest, 1):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        a.sort()
        
        print(a[len(a) - 1] - a[0])
        
    #State: ntest remains unchanged and all test cases have been processed, with the difference between the maximum and minimum values of each list printed for each test case.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an array of integers. For each test case, it calculates and prints the difference between the maximum and minimum values in the array.


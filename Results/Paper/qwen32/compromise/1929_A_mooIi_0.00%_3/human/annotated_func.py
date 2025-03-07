#State of the program right berfore the function call: The input consists of multiple test cases. Each test case starts with an integer n (2 ≤ n ≤ 100) representing the length of the array. This is followed by a line containing n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 10^9) which are the elements of the array. The total number of test cases, t, is between 1 and 500.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        ar = map(str, sorted(list(map(int, input().split()))))
        
        print(' '.join(ar))
        
    #State: For each test case, the output will be a line containing the elements of the array sorted in ascending order, with each element separated by a space. The total number of test cases, t, and the initial state of other variables not affected by the loop remain unchanged.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of an integer `n` and a list of `n` integers. For each test case, it sorts the list of integers in ascending order and prints the sorted list with elements separated by spaces. The function does not modify the input values or maintain any state between test cases.


#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 500. For each test case, n is an integer such that 2 ≤ n ≤ 100, and the second line of each test case contains n integers a_1, a_2, ..., a_n such that 1 ≤ a_i ≤ 10^9.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        ar = map(str, sorted(list(map(int, input().split()))))
        
        print(' '.join(ar))
        
    #State: Output State: The output state will consist of the sorted versions of the lists of integers provided in each test case, with the integers converted to strings and joined by spaces. Each test case's output will be printed on a new line. The number of test cases is determined by the first input, and for each test case, the number of integers \( n \) is provided, followed by the list of \( n \) integers. The integers in each list are sorted in ascending order before being converted to strings and printed.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of a positive integer \( t \) indicating the number of subsequent test cases, followed by an integer \( n \) indicating the number of integers in the list. It then reads \( n \) integers for each test case, sorts them in ascending order, converts each integer to a string, and prints the sorted list as a space-separated string on a new line for each test case. The function implicitly accepts input through standard input and outputs results through standard output.


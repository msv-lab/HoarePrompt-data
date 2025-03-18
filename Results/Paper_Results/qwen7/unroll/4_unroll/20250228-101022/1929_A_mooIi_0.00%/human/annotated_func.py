#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 500. For each test case, n is an integer such that 2 ≤ n ≤ 100, and the second line contains n integers a_1, a_2, ..., a_n such that 1 ≤ a_i ≤ 10^9.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        ar = map(str, sorted(list(map(int, input().split()))))
        
        print(' '.join(ar))
        
    #State: Output State: The output state will consist of multiple lines, each containing n space-separated integers. These integers will be the sorted versions of the input lists provided for each test case, with each element converted to a string. The number of lines will be equal to the number of test cases provided as input. Each line corresponds to the sorted version of the input list for one test case.
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it reads an integer `n` and a list of `n` integers. It sorts the list in ascending order and converts each integer to a string. Then, it prints the sorted list as a single line of space-separated strings. The function handles up to 500 test cases, with each test case containing between 2 and 100 integers, and each integer being between 1 and 10^9. After processing all test cases, the function concludes without returning any value.


#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 500. Each test case consists of n (2 ≤ n ≤ 100) integers representing the array a, where 1 ≤ a_i ≤ 10^9 for all elements in the array.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        ar = map(str, sorted(list(map(int, input().split()))))
        
        print(' '.join(ar))
        
    #State: After all iterations, the output will consist of the sorted versions of the input arrays, each on a new line. The integers within each sorted array will be converted to strings and printed space-separated.
#Overall this is what the function does:The function processes multiple test cases, each containing an array of integers. For each test case, it reads the number of integers `n`, then reads `n` integers from the input, sorts them, converts each integer to a string, and prints them space-separated on a new line. After processing all test cases, the function concludes with the output consisting of sorted arrays from each test case, each on a new line and integers within each array as strings.


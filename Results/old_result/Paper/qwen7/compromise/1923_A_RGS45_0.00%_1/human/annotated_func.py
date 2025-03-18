#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000. For each test case, n is an integer such that 2 ≤ n ≤ 50, and a list of n integers a (a[i] is either 0 or 1) represents the state of each cell where 0 means the cell is free and 1 means the cell contains a chip. Additionally, in each test case, at least one cell contains a chip.
def func():
    t = int(input(''))
    for _ in range(t):
        n = int(input(''))
        
        arr = str(input(''))
        
        x = arr.find('1')
        
        y = arr[::-1].find('1')
        
        z = arr[x:n - y]
        
        print(z.count('0'))
        
    #State: Output State: The output state will consist of the count of '0's between the first and last occurrence of '1' (inclusive of the '1's) for each string `arr` provided in the input, for a total of `t` iterations.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads an integer \( t \) (the number of test cases), an integer \( n \) (the length of the binary string), and a binary string representing the state of \( n \) cells. It then finds the substring between the first and last occurrence of '1' (inclusive) and counts the number of '0's in this substring. The function outputs the count of '0's for each test case.


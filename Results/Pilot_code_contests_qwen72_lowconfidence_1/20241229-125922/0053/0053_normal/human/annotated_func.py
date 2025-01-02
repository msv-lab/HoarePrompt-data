#State of the program right berfore the function call: The function takes no arguments directly, but according to the problem description, it operates on multiple test cases where each test case consists of two arrays of integers a and b, with lengths n and m respectively. The constraints are 1 ≤ n, m ≤ 1000, 1 ≤ a_i, b_i ≤ 1000, and the sum of n and m across all test cases does not exceed 1000.
def func():
    input = lambda : stdin.readline().strip()
    for _ in range(int(input())):
        n, m = [int(i) for i in input().split()]
        
        lst1 = [int(i) for i in input().split()]
        
        lst2 = [int(i) for i in input().split()]
        
        nk = 0
        
        lst1 = set(lst1)
        
        lst2 = set(lst2)
        
        for i in lst1:
            if i in lst2:
                print('YES')
                print(1, i)
                nk = 1
                break
        
        if nk == 0:
            print('NO')
        
    #State of the program after the  for loop has been executed: For each iteration of the loop, `n` and `m` are integers read from the input, representing the lengths of two lists of integers `lst1` and `lst2`, respectively. `lst1` and `lst2` are converted to sets of unique integers. `nk` is a flag that indicates whether any common element was found between `lst1` and `lst2`. If a common element is found, `nk` is set to 1, 'YES' is printed followed by (1, `i`), where `i` is the first common element found, and the inner loop breaks. If no common element is found, `nk` remains 0, and 'NO' is printed. After all iterations, the loop will have processed each test case, printing the appropriate output for each case based on the presence of common elements in the sets `lst1` and `lst2`.
#Overall this is what the function does:The function `func` processes multiple test cases, each consisting of two arrays of integers `a` and `b` with lengths `n` and `m` respectively (1 ≤ n, m ≤ 1000, 1 ≤ a_i, b_i ≤ 1000, and the sum of n and m across all test cases does not exceed 1000). For each test case, it converts the arrays into sets of unique integers. It then checks if there is any common element between the two sets. If a common element is found, it prints 'YES' followed by the common element (specifically, '1' and the common element). If no common element is found, it prints 'NO'. After processing all test cases, the function concludes, having printed the appropriate output for each test case based on the presence of common elements in the sets.


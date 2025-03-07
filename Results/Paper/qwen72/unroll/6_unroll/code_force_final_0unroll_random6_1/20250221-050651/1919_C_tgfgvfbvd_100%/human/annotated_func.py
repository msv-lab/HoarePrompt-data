#State of the program right berfore the function call: The function should take two parameters: an integer t (1 ≤ t ≤ 10^4) representing the number of test cases, and a list of lists, where each inner list contains the integers n (1 ≤ n ≤ 2·10^5) and the elements of the array a (1 ≤ a_i ≤ n). The sum of n over all test cases does not exceed 2·10^5.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        l = list(map(int, input().split()))
        
        a, b = float('inf'), float('inf')
        
        c = 0
        
        for x in range(n):
            if a > b:
                a, b = b, a
            if l[x] <= a:
                a = l[x]
            elif l[x] <= b:
                b = l[x]
            else:
                a = l[x]
                c += 1
        
        print(c)
        
    #State: For each test case, the variable `c` will contain the number of elements in the array `l` that are greater than the two smallest distinct elements found in `l`. The values of `a` and `b` will be the two smallest distinct elements in `l`, if they exist. If there are fewer than two distinct elements, `a` will be the smallest element and `b` will remain `inf`. The loop will print the value of `c` for each test case.
#Overall this is what the function does:The function `func` reads input from the user to process multiple test cases. For each test case, it reads an integer `n` and a list of integers `l`. It then finds the two smallest distinct elements in `l` and counts how many elements in `l` are greater than these two smallest elements. The function prints this count for each test case. The function does not return any value; it only prints the results.


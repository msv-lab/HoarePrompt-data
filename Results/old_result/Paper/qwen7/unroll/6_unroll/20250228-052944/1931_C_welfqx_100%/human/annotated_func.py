#State of the program right berfore the function call: t is a positive integer, and for each test case, n is a positive integer such that 1 ≤ n ≤ 2 ⋅ 10^5, and the array a is a list of n integers where each integer a_i satisfies 1 ≤ a_i ≤ n. Additionally, the sum of all n across all test cases does not exceed 2 ⋅ 10^5.
def func():
    t = int(input())
    for r in range(t):
        n = int(input())
        
        f = 1
        
        num = [int(_) for _ in input().split()]
        
        for j in range(n - 1):
            if num[j] != num[j + 1]:
                f = 0
                break
        
        if n == 1 or f == 1:
            print(0)
            continue
        
        onum = num.copy()
        
        onum.reverse()
        
        cn = 1
        
        ck = 1
        
        f = 1
        
        symb1 = num[0]
        
        symb2 = onum[0]
        
        for i in range(n - 1):
            if num[i] == num[i + 1]:
                cn += 1
            else:
                break
        
        for ii in range(n - 1):
            if onum[ii] == onum[ii + 1]:
                ck += 1
            else:
                break
        
        if symb1 == symb2:
            cn += ck
        
        print(n - max(cn, ck))
        
    #State: Output State: The output state is a series of integers, each representing the value printed for each test case after the loop has executed all its iterations. For each test case, the output is calculated based on the logic inside the loop, which essentially finds the longest consecutive sequence of the same number in both the original and reversed arrays, and then prints the length of the array minus the maximum length of these sequences.
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it reads an integer `t` representing the number of test cases, followed by an integer `n` and a list of `n` integers. It then checks if the list contains any consecutive duplicates. If the list has only one element or no consecutive duplicates, it prints `0`. Otherwise, it calculates the lengths of the longest consecutive sequences in both the original and reversed lists, sums these lengths if the first elements of both sequences are the same, and prints the difference between the length of the list and this sum.


#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 1 ≤ n ≤ 3 \cdot 10^5, and the array a is a list of n integers where each integer a_i satisfies 1 ≤ a_i ≤ n. The sum of n over all test cases does not exceed 3 \cdot 10^5.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        ar = list(map(int, input().split()))
        
        same = 1
        
        num = ar[0]
        
        minn = inf
        
        i = 1
        
        while i < len(ar):
            if ar[i] == num:
                same += 1
            else:
                i += 1
                num = ar[i]
                minn = min(minn, same)
                same = 1
            i += 1
        
        minn = min(minn, same)
        
        if minn == inf:
            print(-1)
        else:
            print(minn)
        
    #State: The final value of `minn` is determined as the minimum count of consecutive occurrences of any number in the entire list `ar` across all iterations. `same` holds the count of consecutive occurrences of the current number being processed, `num` is the current number being considered, and `i` is equal to the length of the list `ar`.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer \( n \) and an array \( a \) of \( n \) integers. For each test case, it calculates the minimum count of consecutive occurrences of any number in the array \( a \). If no such sequence exists, it prints -1; otherwise, it prints the minimum count. The function does not return any value but prints the result for each test case.


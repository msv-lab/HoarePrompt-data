#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4; for each test case, n is a positive integer such that 1 ≤ n ≤ 2⋅10^5; the list a contains n positive integers such that 1 ≤ a_i ≤ 10^9 for each a_i, and the sum of all n values across all test cases does not exceed 2⋅10^5.
def func():
    t = int(input())
    for i in range(t):
        n = int(input())
        
        l = map(int, input().split())
        
        lis = sorted(set(l))
        
        if 1 not in lis or len(lis) == 1:
            print('Alice')
        else:
            test = True
            for j in range(1, len(lis)):
                if lis[j] - lis[j - 1] > 1:
                    if j % 2 == 1:
                        print('Bob')
                    else:
                        print('Alice')
                    test = False
                    break
            if test == True:
                if len(lis) % 2 == 1:
                    print('Alice')
                else:
                    print('Bob')
        
    #State: Output State: Alice or Bob is printed based on the conditions met within each test case. For each test case, if the list `lis` contains only one unique number or does not contain the number 1, 'Alice' is printed. Otherwise, if there is a gap greater than 1 between any two consecutive numbers in `lis`, 'Bob' is printed if the position of the gap is odd, and 'Alice' is printed otherwise. If no such gap exists, 'Alice' is printed if the length of `lis` is odd, and 'Bob' is printed if it is even.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads an integer t, followed by an integer n and a list of n positive integers. It then determines and prints either 'Alice' or 'Bob' based on specific conditions related to the sorted unique elements of the list. If the list contains only one unique number or does not contain the number 1, it prints 'Alice'. If there is a gap greater than 1 between any two consecutive numbers in the sorted unique list, it prints 'Bob' if the position of the gap is odd, and 'Alice' if it is even. If no such gap exists, it prints 'Alice' if the length of the sorted unique list is odd, and 'Bob' if it is even.


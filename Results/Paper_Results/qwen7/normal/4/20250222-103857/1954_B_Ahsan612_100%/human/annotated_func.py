#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 1 ≤ n ≤ 3 ⋅ 10^5, and the array a is a list of n integers where 1 ≤ a_i ≤ n. Additionally, the sum of n over all test cases does not exceed 3 ⋅ 10^5.
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
        
        if minn == inf or minn == len(ar):
            print(-1)
        else:
            print(minn)
        
    #State: Output State: After the loop executes all the iterations, `minn` will hold the minimum value of the longest sequence of consecutive identical elements in the array `ar`. `same` will be 1 because it is reset to 1 at the start of each new sequence of identical elements. `i` will be equal to `len(ar)`, indicating that the entire array has been processed. `num` will be the last element of the array `ar` that was checked before the loop ended. If `minn` was never updated during the loop or was set to infinity initially, `minn` will still be infinity. Otherwise, `minn` will be the smallest value among the lengths of sequences of consecutive identical elements found in the array.
    #
    #The output will be `-1` if `minn` is infinity or equal to the length of the array, indicating that there are no sequences of consecutive identical elements. Otherwise, the output will be the value of `minn`, which is the length of the shortest sequence of consecutive identical elements in the array.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer \( t \) (number of test cases), an integer \( n \) (length of the array), and an array \( a \) of \( n \) integers. For each test case, it finds the length of the shortest sequence of consecutive identical elements in the array \( a \). If no such sequence exists, it outputs -1. Otherwise, it outputs the length of the shortest such sequence.


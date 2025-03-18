#State of the program right berfore the function call: The function should take two parameters: an integer t (1 ≤ t ≤ 10^4) representing the number of test cases, and a list of lists, where each sublist contains integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ n) and the length of each sublist n (1 ≤ n ≤ 3 · 10^5) is provided in the first element of the sublist. Additionally, in every test case, the given array a is beautiful, and the sum of n over all test cases does not exceed 3 · 10^5.
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
        
    #State: `t` is an integer (1 ≤ t ≤ 10^4), `n` is the last input integer greater than 0, `ar` is the last list of integers provided by the user input, `i` is equal to `len(ar)`, `num` is the last unique number in the list `ar`, `same` is the count of consecutive occurrences of `num` at the end of the list, and `minn` is the minimum value of the counts of consecutive occurrences of any number in the list `ar`. If `minn` was initially `inf`, then `minn` is updated to the smallest count of consecutive occurrences found in the list. Otherwise, `minn` remains the minimum value between the original `minn` and the smallest count of consecutive occurrences found in the list.
#Overall this is what the function does:The function reads multiple test cases from user input. For each test case, it reads an integer `n` and a list of integers `ar` of length `n`. It then calculates the minimum length of consecutive sequences of the same number in `ar`. If no such sequence exists, it prints `-1`. Otherwise, it prints the minimum length of these sequences. The function does not return any value; it only prints the results for each test case.


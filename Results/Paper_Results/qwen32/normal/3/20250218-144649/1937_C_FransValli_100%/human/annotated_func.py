#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^3, and for each test case, n is an integer such that 2 <= n <= 10^4. The sum of n over all test cases does not exceed 10^4. The sequence p_0, p_1, ..., p_{n-1} is a permutation of {0, 1, ..., n-1}.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        maxi = 0
        
        for i in range(1, n):
            print('?', maxi, maxi, i, i, flush=True)
            res = input()
            if res == '<':
                maxi = i
        
        arr = [0]
        
        for i in range(1, n):
            print('?', maxi, arr[0], maxi, i, flush=True)
            res = input()
            if res == '<':
                arr = [i]
            elif res == '=':
                arr.append(i)
        
        mini = arr[0]
        
        for item in arr[1:]:
            print('?', mini, mini, item, item, flush=True)
            res = input()
            if res == '>':
                mini = item
        
        print('!', maxi, mini, flush=True)
        
    #State: t is an integer such that 1 <= t <= 10^3, n is an integer such that 2 <= n <= 10^4, and for each test case, maxi is the index of the largest element in the permutation p_0, p_1, ..., p_{n-1}, mini is the index of the smallest element in the permutation, and the loop has finished processing all test cases.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `n` and a permutation `p` of integers from 0 to `n-1`. For each test case, it identifies and outputs the indices of the largest and smallest elements in the permutation.


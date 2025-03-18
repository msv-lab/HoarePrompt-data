#State of the program right berfore the function call: None of the input variables are explicitly defined in the provided function signature. However, based on the problem description, t (the number of test cases) is an integer such that 1 ≤ t ≤ 10^3, and for each test case, n (the size of the permutation) is an integer such that 2 ≤ n ≤ 10^4. Additionally, the permutation p_0, p_1, ..., p_{n-1} is a permutation of {0, 1, ..., n-1}.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        mak = 0
        
        for i in range(1, n):
            print('?', mak, mak, i, i)
            sys.stdout.flush()
            if str(input()) == '<':
                mak = i
        
        mak2 = mak
        
        pans = []
        
        for i in range(n):
            print('?', mak, mak2, i, mak2)
            sys.stdout.flush()
            s = str(input())
            if s == '<':
                mak = i
                pans = [i]
            elif s == '=':
                pans.append(i)
        
        mak = 0
        
        for i in range(1, len(pans)):
            print('?', pans[mak], pans[mak], pans[i], pans[i])
            sys.stdout.flush()
            if str(input()) == '>':
                mak = i
        
        print('!', mak2, pans[mak])
        
        sys.stdout.flush()
        
    #State: Output State: The output state will consist of two integers separated by a space. The first integer represents the value of `mak2`, which is the final value of `mak` after the second main loop completes. The second integer is the value of `pans[mak]`, which is the last element in the list `pans` that satisfies the condition of being equal to or greater than `mak2`. This result is derived from the interactions with the hypothetical comparison oracle through the `?` and `!` commands, where the program queries the relative order between pairs of indices and outputs the final determined order.
#Overall this is what the function does:The function processes a series of test cases, each involving a permutation of integers. For each test case, it queries the relative order between pairs of indices using a hypothetical comparison oracle. It determines the final value of `mak2` and the last element in the list `pans` that satisfies the condition of being equal to or greater than `mak2`. The function then outputs these two values, representing the final determined order of the permutation for each test case.


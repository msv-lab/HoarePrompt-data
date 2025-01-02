#State of the program right berfore the function call: N is an integer such that 2 ≤ N ≤ 100, and a is a list of N integers where each integer a_i satisfies 1 ≤ a_i ≤ N-1.
def func():
    n = int(raw_input())
    a = map(int, raw_input().split())
    maxa = max(a)
    cmaxa = a.count(maxa)
    ca = [0] * (maxa + 1)
    for i in xrange(n):
        ca[a[i]] += 1
        
    #State of the program after the  for loop has been executed: `N` is an integer such that 2 ≤ N ≤ 100, `n` is an input integer such that 2 ≤ n ≤ 100, `a` is a list of integers read from the input, `maxa` is the maximum value in `a`, `cmaxa` is the number of times `maxa` appears in `a`, `ca` is a list of length `maxa + 1` where each element at index `x` represents the count of occurrences of `x` in `a`.
    if (maxa % 2 == 1) :
        l = maxa / 2 + 1
        if (a.count(l) == 2) :
            for i in xrange(n):
                if a[i] < l:
                    print('Impossible')
                    exit()
                
            #State of the program after the  for loop has been executed: `N` is an integer such that 2 ≤ N ≤ 100, `n` is an input integer such that 2 ≤ n ≤ 100, `a` is a list of integers read from the input, `maxa` is the maximum value in `a` and is odd, `cmaxa` is the number of times `maxa` appears in `a`, `ca` is a list of length `maxa + 1` where each element at index `x` represents the count of occurrences of `x` in `a`, `l` is a float equal to `maxa / 2 + 1`, the number of occurrences of `l` in `a` is exactly 2, `i` is `n - 1`. If any `a[i] < l` for 0 ≤ i < n, the program has terminated with the message 'Impossible'. Otherwise, all elements in `a` are such that `a[i] >= l` for 0 ≤ i < n.
            for i in xrange(l + 1, maxa + 1):
                if ca[i] < 2:
                    print('Impossible')
                    exit()
                
            #State of the program after the  for loop has been executed: `N` is an integer such that 2 ≤ N ≤ 100, `n` is an input integer such that 2 ≤ n ≤ 100, `a` is a list of integers read from the input, `maxa` is the maximum value in `a` and is odd, `cmaxa` is the number of times `maxa` appears in `a`, `ca` is a list of length `maxa + 1` where each element at index `x` represents the count of occurrences of `x` in `a`, `l` is a float equal to `maxa / 2 + 1`, the number of occurrences of `l` in `a` is exactly 2, `i` is `n - 1`. For all values `i` in the range `l + 1` to `maxa + 1`, `ca[i]` is at least 2. If any `ca[i]` is less than 2, the program has terminated with the message 'Impossible'.
            print('Possible')
        else :
            print('Impossible')
        #State of the program after the if-else block has been executed: *`N` is an integer such that 2 ≤ N ≤ 100, `n` is an input integer such that 2 ≤ n ≤ 100, `a` is a list of integers read from the input, `maxa` is the maximum value in `a` and is odd, `cmaxa` is the number of times `maxa` appears in `a`, `ca` is a list of length `maxa + 1` where each element at index `x` represents the count of occurrences of `x` in `a`, `l` is a float equal to `maxa / 2 + 1`. If the number of occurrences of `l` in `a` is exactly 2, then for all values `i` in the range `l + 1` to `maxa + 1`, `ca[i]` is at least 2. If any `ca[i]` is less than 2, the program has terminated with the message 'Impossible'. Otherwise, the string 'Possible' has been printed. If the count of `l` in `a` is not equal to 2, 'Impossible' is printed.
    else :
        l = maxa / 2
        if (a.count(l) == 1) :
            for i in xrange(n):
                if a[i] < l:
                    print('Impossible')
                    exit()
                
            #State of the program after the  for loop has been executed: `N` is an integer such that 2 ≤ N ≤ 100, `n` is an input integer such that 2 ≤ n ≤ 100, `a` is a list of integers read from the input, `maxa` is the maximum value in `a`, `cmaxa` is the number of times `maxa` appears in `a`, `ca` is a list of length `maxa + 1` where each element at index `x` represents the count of occurrences of `x` in `a`, `maxa` is even, `l` is `maxa / 2`, the count of `l` in `a` is 1, `i` is `n-1`. For all elements `a[j]` in `a` where `0 ≤ j < n`, `a[j]` is greater than or equal to `l`. If any `a[j]` is less than `l`, 'Impossible' is printed, and the program has terminated.
            for i in xrange(l + 1, maxa + 1):
                if ca[i] < 2:
                    print('Impossible')
                    exit()
                
            #State of the program after the  for loop has been executed: `N` is an integer such that 2 ≤ N ≤ 100, `n` is an input integer such that 2 ≤ n ≤ 100, `a` is a list of integers read from the input, `maxa` is the maximum value in `a`, `cmaxa` is the number of times `maxa` appears in `a`, `ca` is a list of length `maxa + 1` where each element at index `x` represents the count of occurrences of `x` in `a`, `maxa` is even, `l` is `maxa / 2`, the count of `l` in `a` is 1, `i` is `maxa + 1`, for all elements `a[j]` in `a` where `0 ≤ j < n`, `a[j]` is greater than or equal to `l`. If any `a[j]` is less than `l`, 'Impossible' is printed, and the program has terminated. If for any `i` in the range `l + 1` to `maxa`, `ca[i]` is less than 2, 'Impossible' is printed, and the program has terminated. Otherwise, the program continues with the original state unchanged.
            print('Possible')
        else :
            print('Impossible')
        #State of the program after the if-else block has been executed: *`N` is an integer such that 2 ≤ N ≤ 100, `n` is an input integer such that 2 ≤ n ≤ 100, `a` is a list of integers read from the input, `maxa` is the maximum value in `a`, `cmaxa` is the number of times `maxa` appears in `a`, `ca` is a list of length `maxa + 1` where each element at index `x` represents the count of occurrences of `x` in `a`, `maxa` is even, `l` is `maxa / 2`. If `a.count(l)` is 1, `i` is `maxa + 1`, for all elements `a[j]` in `a` where `0 ≤ j < n`, `a[j]` is greater than or equal to `l`, if any `a[j]` is less than `l`, 'Impossible' is printed, and the program has terminated. If for any `i` in the range `l + 1` to `maxa`, `ca[i]` is less than 2, 'Impossible' is printed, and the program has terminated. Otherwise, 'Possible' is printed. If `a.count(l)` is not 1, 'Impossible' is printed to the console.
    #State of the program after the if-else block has been executed: *`N` is an integer such that 2 ≤ N ≤ 100, `n` is an input integer such that 2 ≤ n ≤ 100, `a` is a list of integers read from the input, `maxa` is the maximum value in `a`, `cmaxa` is the number of times `maxa` appears in `a`, `ca` is a list of length `maxa + 1` where each element at index `x` represents the count of occurrences of `x` in `a`. If `maxa` is odd, `l` is a float equal to `maxa / 2 + 1`. If the number of occurrences of `l` in `a` is exactly 2, then for all values `i` in the range `l + 1` to `maxa + 1`, `ca[i]` is at least 2. If any `ca[i]` is less than 2, the program prints 'Impossible' and terminates. Otherwise, the program prints 'Possible'. If the count of `l` in `a` is not equal to 2, 'Impossible' is printed. If `maxa` is even, `l` is `maxa / 2`. If `a.count(l)` is 1, for all elements `a[j]` in `a` where `0 ≤ j < n`, `a[j]` is greater than or equal to `l`. If any `a[j]` is less than `l`, 'Impossible' is printed, and the program terminates. If for any `i` in the range `l + 1` to `maxa`, `ca[i]` is less than 2, 'Impossible' is printed, and the program terminates. Otherwise, 'Possible' is printed. If `a.count(l)` is not 1, 'Impossible' is printed to the console.
#Overall this is what the function does:The function reads two inputs: an integer `n` (2 ≤ n ≤ 100) and a list of `n` integers `a` (1 ≤ a_i ≤ n-1). It then determines whether the list `a` meets certain conditions based on the maximum value in `a` (`maxa`) and a derived value `l`. The conditions are as follows:

1. If `maxa` is odd:
   - `l` is set to `maxa / 2 + 1`.
   - The function checks if `l` appears exactly twice in `a`.
   - If `l` appears exactly twice, the function further checks if all elements in `a` are greater than or equal to `l`.
   - Additionally, it checks if for all values `i` in the range `l + 1` to `maxa + 1`, the count of `i` in `a` is at least 2.
   - If both conditions are met, the function prints 'Possible'. If any condition fails, the function prints 'Impossible' and exits.

2. If `maxa` is even:
   - `l` is set to `maxa / 2`.
   - The function checks if `l` appears exactly once in `a`.
   - If `l` appears exactly once, the function further checks if all elements in `a` are greater than or equal to `l`.
   - Additionally, it checks if for all values `i` in the range `l + 1` to `maxa + 1`, the count of `i` in `a` is at least 2.
   - If both conditions are met, the function prints 'Possible'. If any condition fails, the function prints 'Impossible' and exits.

If any of the conditions are not met, the function prints 'Impossible' and exits. If all conditions are met, the function prints 'Possible' and the program continues.


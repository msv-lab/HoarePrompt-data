#State of the program right berfore the function call: This is an interactive problem with no explicit input variables defined in the function signature. The problem involves finding two indices i and j in a secret permutation p such that p_i \oplus p_j is maximized using at most 3n queries. The permutation p is a sequence of unique integers from 0 to n-1, and n is an integer such that 2 \leq n \leq 10^4.
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
        
    #State: Output State: The output state is the result of finding two indices \( i \) and \( j \) in a secret permutation \( p \) such that \( p_i \oplus p_j \) is maximized using at most 3n queries. After executing the loop, the values of \( maxi \) and \( mini \) are printed as the result, where \( maxi \) is the index of the maximum value in the permutation and \( mini \) is the index of the minimum value in the permutation found through the comparison process described in the loop.
#Overall this is what the function does:The function finds two indices \(i\) and \(j\) in a secret permutation \(p\) such that \(p_i \oplus p_j\) is maximized using at most \(3n\) queries. It first identifies an index \(maxi\) with a high value, then determines an index \(mini\) with a low value among those compared to \(maxi\). Finally, it outputs these two indices \(maxi\) and \(mini\).


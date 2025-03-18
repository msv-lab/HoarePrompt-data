#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, n is an integer such that 1 <= n <= 100, f and k are integers such that 1 <= f, k <= n, and a is a list of n integers where each integer a_i satisfies 1 <= a_i <= 100.
def func():
    t = int(input())
    for i in range(t):
        a = input()
        
        b = list(map(int, a.split()))
        
        o = input().split()
        
        n = b[0]
        
        f = b[1]
        
        k = b[2]
        
        if k == n:
            print('YES')
            continue
        
        fav = o[f - 1]
        
        dic = {i: o.count(i) for i in o}
        
        o.sort(reverse=True)
        
        if o.index(fav) > k - 1:
            print('NO')
            continue
        
        l = sorted(list(set(o)), reverse=True)
        
        for i in range(len(l)):
            if fav != l[i]:
                k -= dic[l[i]]
                if k <= 0:
                    print('NO')
                    break
            else:
                k -= dic[l[i]]
                if k < 0:
                    print('MAYBE')
                    break
                else:
                    print('YES')
                    break
        
    #State: `t` is 0, `i` is the length of the list `l` for the last iteration, `a` is the last input string, `b` is the list of integers obtained by splitting the last `a` and converting each element to an integer, `o` is the list of strings obtained from the last input, now sorted in descending order, `n` is the first integer in the last list `b`, `f` is the second integer in the last list `b`, `k` is updated based on the loop's logic for the last iteration, `fav` is the string at the index `f - 1` in the list `o` before it was sorted, `dic` is a dictionary where each key is a string from `o` and each value is the count of how many times that string appears in `o`, and `l` is a list of unique strings from `o` sorted in descending order.
#Overall this is what the function does:The function reads multiple sets of inputs, each set consisting of an integer `n`, two integers `f` and `k`, and a list of `n` integers. It then checks if the favorite integer (at index `f-1` in the list) can be among the top `k` integers when the list is sorted in descending order. For each set of inputs, it prints 'YES' if the favorite integer is among the top `k`, 'NO' if it is not, and 'MAYBE' if it is among the top `k` but the exact position is uncertain due to ties. After processing all sets, the function terminates.


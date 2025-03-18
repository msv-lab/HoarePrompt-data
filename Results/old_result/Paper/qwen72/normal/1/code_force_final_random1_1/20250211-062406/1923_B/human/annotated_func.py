#State of the program right berfore the function call: a is a list of positive integers representing the health of each monster, x is a list of non-zero integers representing the initial positions of the monsters, and k is a positive integer representing the maximum number of bullets you can fire per second. The lengths of a and x are equal, and each element in x is unique and sorted in ascending order.
def func_1(a, x, k):
    n = len(a)
    sorted_indices = sorted(range(n), key=lambda i: abs(x[i]))
    distance = 0
    pos = 0
    while pos != len(sorted_indices):
        if abs(x[sorted_indices[pos]]) == distance:
            return False
        
        rest = k
        
        while rest != 0 and pos != len(sorted_indices):
            delta = min(rest, a[sorted_indices[pos]])
            rest -= delta
            a[sorted_indices[pos]] -= delta
            if a[sorted_indices[pos]] == 0:
                pos += 1
        
        distance += 1
        
    #State: After all iterations of the loop, `a` will contain the remaining health of each monster, with some elements possibly being 0 if those monsters have been defeated. `rest` will be 0, indicating that no more bullets are left to fire. `pos` will be equal to the number of monsters that have been defeated, which is also the number of elements in `a` that are 0. The absolute value of the element at the index `sorted_indices[pos]` in `x` will still not be equal to `distance + 1`, assuming there are any monsters left with positive health. `distance` will be the final distance value after all iterations, which is the number of unique distances covered by the loop. The values of `x`, `k`, `n`, and `sorted_indices` remain unchanged.
    return True
    #The program returns True.
#Overall this is what the function does:The function `func_1` takes three parameters: `a` (a list of positive integers representing the health of each monster), `x` (a list of non-zero integers representing the initial positions of the monsters), and `k` (a positive integer representing the maximum number of bullets you can fire per second). It processes the monsters in increasing order of their absolute positions. For each distance, it attempts to reduce the health of the monsters at that distance using up to `k` bullets. If at any point a monster reaches the position 0 (i.e., its absolute position equals the current distance), the function returns `False`. If all monsters are defeated before any monster reaches position 0, the function returns `True`. After the function concludes, the list `a` will contain the remaining health of each monster, with some elements possibly being 0 if those monsters have been defeated. The lists `x` and `k` remain unchanged.

#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 3 · 10^4. n and k are positive integers such that 1 ≤ n ≤ 3 · 10^5 and 1 ≤ k ≤ 2 · 10^9. a is a list of n positive integers where 1 ≤ a_i ≤ 10^9. x is a list of n integers where -n ≤ x_1 < x_2 < ... < x_n ≤ n and x_i ≠ 0.
def func_2():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        
        a = list(map(int, input().split()))
        
        x = list(map(int, input().split()))
        
        print('YES' if func_1(a, x, k) else 'NO')
        
    #State: `t` is 0, `n` and `k` are specific integers provided by the user, `a` is a list of integers provided by the last user input, `x` is a list of integers converted from the last user input.
#Overall this is what the function does:The function `func_2` reads multiple sets of inputs from the user, each set consisting of two integers `n` and `k`, a list of integers `a`, and a list of integers `x`. For each set of inputs, it calls another function `func_1` with `a`, `x`, and `k` as arguments. If `func_1` returns `True`, it prints 'YES'; otherwise, it prints 'NO'. After processing all sets of inputs (determined by `t`), the function completes its execution. The final state of the program is that `t` is 0, and the last values of `n`, `k`, `a`, and `x` are those from the last set of inputs processed.


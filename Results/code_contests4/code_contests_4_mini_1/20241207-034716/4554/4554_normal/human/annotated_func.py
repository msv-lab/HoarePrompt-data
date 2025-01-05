#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 13,845, and a_i are integers for i from 1 to n, where -336 ≤ a_i ≤ 1164, and the sum of all a_i is equal to 0.
def func():
    n = int(input())
    a = []
    for i in range(n):
        x = int(input())
        
        a.append(x)
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 2 ≤ `n` ≤ 13,845; `i` is `n - 1`; `a` contains `n` integers input by the user.
    b = []
    count = 0
    for i in range(n):
        if a[i] % 2 == 0:
            b.append(a[i] / 2)
        
        if a[i] % 2 != 0:
            count = count + 1
            if count % 2 == 1:
                a[i] = a[i] / 2
                b.append(a[i])
            if count % 2 == 0:
                a[i] = a[i] / 2 + 1
                b.append(a[i])
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 2 ≤ `n` ≤ 13,845; `count` is the number of odd integers in `a`; `b` contains half of each even integer in `a` and modified values of odd integers in `a` based on their positions; `a` is modified with updated values for odd integers.
    print(b)
#Overall this is what the function does:The function accepts an integer input `n` (where 2 ≤ n ≤ 13,845) and subsequently reads `n` integer values, `a_i` (where -336 ≤ a_i ≤ 1164) that sum to 0. It processes these integers by dividing even integers by 2 and modifying odd integers based on their position: for odd integers at odd positions, it divides by 2, while for odd integers at even positions, it divides by 2 and adds 1. The processed integers are then stored in a list `b`, which is printed at the end. The function does not return any values but outputs the list `b` to the console.


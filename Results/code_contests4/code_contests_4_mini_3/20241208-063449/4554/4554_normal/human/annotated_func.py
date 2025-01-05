#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 13845, and a_i is an integer for each participant i (1 ≤ i ≤ n) satisfying -336 ≤ a_i ≤ 1164, with the sum of all a_i equal to 0.
def func():
    n = int(input())
    a = []
    for i in range(n):
        x = int(input())
        
        a.append(x)
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 2 ≤ `n` ≤ 13845; `a` is a list containing `n` integers; `i` is `n - 1`
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
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 2 ≤ `n` ≤ 13845; `i` is `n - 1`; `b` is a list containing the values of half of all elements from `a`, where even elements are halved and odd elements are halved with an increment of 1 based on their count in `a`; `count` is the number of odd integers in `a`.
    print(b)
#Overall this is what the function does:The function accepts an integer input `n`, where `n` is between 2 and 13845, and subsequently reads `n` integers from the input, which are each constrained between -336 and 1164, with their total sum equal to 0. It processes these integers by halving even integers directly and halving odd integers with an adjustment based on their order of appearance, storing the results in a new list `b`. The function then prints the list `b`, which contains the processed values of half of all elements from the input list. Note that the function does not return any value; it only prints the output.


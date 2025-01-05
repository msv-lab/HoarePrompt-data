#State of the program right berfore the function call: **
def func():
    n = int(input())
    a = []
    for i in range(n):
        x = int(input())
        
        a.append(x)
        
    #State of the program after the  for loop has been executed: `n` is greater than 0, `a` is a list containing `n` input integers, `i` is equal to `n-1`
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
        
    #State of the program after the  for loop has been executed: `n` is greater than 0, `a` is a list containing `n` modified input integers based on the conditions in the loop, `i` is equal to `n-1`, `b` is a list containing elements from `a` that meet the specified conditions in the loop, `count` is the number of elements in `a` that are not divisible by 2 or the count of odd numbers in `a`.
    print(b)
#Overall this is what the function does:The function takes user input for the number of elements, then prompts the user to input integers which are stored in a list. It iterates over the list elements, performs specific operations based on whether the element is divisible by 2 or not, and modifies the elements accordingly. The final list `b` contains elements that meet the specified conditions. Finally, it prints list `b`. The function does not accept any parameters and performs input/output operations based on the user's inputs.


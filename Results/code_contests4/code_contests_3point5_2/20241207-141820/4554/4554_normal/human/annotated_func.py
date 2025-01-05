#State of the program right berfore the function call: **
def func():
    n = int(input())
    a = []
    for i in range(n):
        x = int(input())
        
        a.append(x)
        
    #State of the program after the  for loop has been executed: `n` is greater than 0, `a` contains `n` elements with the values input by the user, `i` is `n-1`
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
        
    #State of the program after the  for loop has been executed: `n` is greater than 0, `a` contains `n` elements with values input by the user, `i` is -1, `b` is a list containing elements from the operations in the loop, `count` reflects the total number of elements in `b`
    print(b)
#Overall this is what the function does:The function does not accept any parameters. It prompts the user to input a number `n`, then inputs `n` integers into a list `a`. It then performs different operations on the elements of `a` based on their divisibility by 2 and the count of odd elements. The modified elements are stored in a list `b`, and finally, the function prints the list `b`.


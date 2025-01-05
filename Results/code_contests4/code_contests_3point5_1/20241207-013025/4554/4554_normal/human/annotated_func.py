#State of the program right berfore the function call: n is an integer such that 2 <= n <= 13845. Each a_i is an integer such that -336 <= a_i <= 1164, and the sum of all a_i is equal to 0.**
def func():
    n = int(input())
    a = []
    for i in range(n):
        x = int(input())
        
        a.append(x)
        
    #State of the program after the  for loop has been executed: `a` is a list containing `n` integers entered through input, `i` is equal to `n-1`, `x` is the last integer entered
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
        
    #State of the program after the  for loop has been executed: `a` is a list containing updated integers, `i` is equal to the last index of list `a`, `x` is the last integer entered in the updated list `a`, `b` is a list containing the integer results of the divisions and updates based on the conditions in the loop, `count` is the total number of elements in list `a` that were odd before the loop executed.
    print(b)
#Overall this is what the function does:The function takes an input `n` and then prompts the user to input `n` integers. It processes the input integers based on certain conditions: if the integer is even, it divides it by 2 and adds the result to a list `b`. If the integer is odd, it alternates between dividing by 2 and dividing by 2 and adding 1, based on the count of odd numbers encountered so far. The function then prints the list `b`. However, the annotations mention constraints and conditions that are not fully implemented in the code, such as ensuring the sum of all input integers is equal to 0. The current code does not enforce this constraint.


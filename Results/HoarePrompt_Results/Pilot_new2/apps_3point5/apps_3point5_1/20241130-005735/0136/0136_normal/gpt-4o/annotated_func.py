#State of the program right berfore the function call: There are no specific preconditions for this problem.
def func_1():
    data = input().split()
    a = data[0].lstrip('0')
    b = data[1].lstrip('0')
    if (not a) :
        a = '0'
    #State of the program after the if block has been executed: *`data` is a list containing the values entered as input and separated by spaces. `a` is the string '0' with leading zeros removed. `b` is the second element of `data` with leading zeros removed. After entering the if condition, `a` evaluates to False.
    if (not b) :
        b = '0'
    #State of the program after the if block has been executed: *`data` is a list containing the values entered as input and separated by spaces. `a` is the string '0' with leading zeros removed. `b` is the string '0' with leading zeros removed. After entering the if condition, `a` evaluates to False. The current value of `b` results in a False evaluation when used in the `not` operation.
    if (len(a) < len(b)) :
        print('<')
    else :
        if (len(a) > len(b)) :
            print('>')
        else :
            if (a < b) :
                print('<')
            else :
                if (a > b) :
                    print('>')
                else :
                    print('=')
                #State of the program after the if-else block has been executed: *`data` is a list containing the input values. `a` is the string '0' with leading zeros removed. `b` is the string '0' with leading zeros removed. The length of `a` is not less than the length of `b`. The current value of `b` does not result in a True evaluation when used in the `not` operation. The condition (len(a) > len(b)) is false after not entering the if block, `a` is not less than `b`, and after the if block, the value of `a` is greater than `b`. However, if `a` is not greater than `b`, `a` is not less than `b`, and (a <= b).
            #State of the program after the if-else block has been executed: *`data` is a list containing the input values. `a` and `b` are strings with leading zeros removed. The length of `a` is not less than the length of `b`. The current value of `b` does not result in a True evaluation when used in the `not` operation. The condition (len(a) > len(b)) is false after not entering the if block. If `a` is less than `b`, '<' is printed. If `a` is not less than `b` and is also not greater than `b`, then `a` is not less than `b`. If `a` is not less than `b` and `a` is greater than `b`, then `a` is greater than `b` after the execution of the if else block.
        #State of the program after the if-else block has been executed: *`data` is a list containing the input values. `a` and `b` are strings with leading zeros removed. The length of `a` is not less than the length of `b`. The current value of `b` does not result in a True evaluation when used in the `not` operation. After the execution of the if else block, if `a` is less than `b`, '<' is printed. If `a` is not less than `b` and is also not greater than `b`, then `a` is not less than `b`. If `a` is not less than `b` and `a` is greater than `b`, then `a` is greater than `b`.
    #State of the program after the if-else block has been executed: *`data` is a list containing the input values. `a` and `b` are strings with leading zeros removed. If the length of `a` is less than the length of `b`, the program prints '<'. If the length of `a` is not less than the length of `b`, and `a` is not less than `b`, the program will not print anything. If `a` is not less than `b` and `a` is greater than `b`, the program will not print anything.
#Overall this is what the function does:The function func_1 does not have any specific preconditions and does not accept any parameters. It reads input data, removes leading zeros from two strings a and b, and then compares the lengths of a and b. If the length of a is less than the length of b, it prints '<'. If the length of a is equal to the length of b, it compares the values of a and b, printing '<' if a is less than b, '>' if a is greater than b, and '=' if a is equal to b. The function does not return any specific value.


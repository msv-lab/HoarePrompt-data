#State of the program right berfore the function call: **Precondition**: **A is an integer such that 1 <= A <= 105.**
def func():
    n = int(sys.stdin.readline().rstrip('\n'))
    change = 1000000
    nom = [1]
    if (n <= 10) :
        for x in range(1000001 - 1, 0, -1):
            if len(nom) == n:
                break
            
            nom.append(x)
            
        #State of the program after the  for loop has been executed: `n` is an integer input from the standard input within the range of 1 to 10, `change` is 1000000, `nom` is a list containing integers 1 to `n` in descending order from 1000000 to 1000000 - `n` + 1.
    else :
        if (10 < n <= 100) :
            res = n - n % 10 - 1
            res_ = change // res
            nom.append(res_)
            for x in range(1000000 - 1, 0, -1):
                if len(nom) == 10:
                    break
                
                nom.append(x)
                
            #State of the program after the  for loop has been executed: `n` is an integer input from 11 to 105, `change` is 1000000, `nom` contains the integer 1 followed by the values of `res_`, `x` is 0, the length of `nom` is 10 or more
        else :
            if (100 < n <= 1000) :
                res = n - n % 10 - 1
                res_ = change // res
                nom.append(res_)
                for x in range(1000000 - 1, 0, -1):
                    if len(nom) == 10:
                        break
                    elif len(nom) == n % 10 + 2:
                        break
                    
                    nom.append(x)
                    
                #State of the program after the  for loop has been executed: `n` is an integer input from the standard input within the range of 11 to 105, `change` is 1000000, `nom` contains the integer 1 and a specific integer based on input `n`. If `n` is less than 10, `nom` will have 10 elements starting from 1 to 10. If `n` is greater than or equal to 10, `nom` will have `n % 10 + 2` elements.
            else :
                if (1000 < n <= 10000) :
                    if (n == 10000) :
                        change = 10000
                        print(str(change) + ' ' + str(2))
                        print(str(1) + ' ' + str(9))
                        exit(0)
                    #State of the program after the if block has been executed: *`n` is an integer input from the standard input within the range of 11 to 105, `change` is 1000000, `nom` is a list containing the integer 1. n is not within the range of 11 to 100 and n is not between 100 and 1000. Additionally, n is an integer where 1000 < n <= 10000. If n == 10000, the program sets `change` to 10000, updates `nom` to contain the integer 1, and prints '10000 2'.
                    res = n - n % 10 - 1
                    res_ = change // res
                    nom.append(res_)
                    for x in range(1000000 - 1, 0, -1):
                        if len(nom) == 10:
                            break
                        elif len(nom) == n % 10 + 2:
                            break
                        
                        nom.append(x)
                        
                    #State of the program after the  for loop has been executed: `n` is an integer from 11 to 105, `change` is 1000000, `nom` contains integers with a length equal to the last digit of `n` plus 2
                else :
                    if (10000 < n <= 100000) :
                        if (n == 100000) :
                            change = 100000
                            print(str(change) + ' ' + str(2))
                            print(str(1) + ' ' + str(9))
                            exit(0)
                        #State of the program after the if block has been executed: *`n` is an integer input from the standard input within the range of 11 to 105, `change` is 1000000, `nom` is a list containing the integer 1, `n` is an integer where 10000 < n <= 100000. If n == 100000, the code prints '1000000 2'.
                        res = n - n % 10 - 1
                        res_ = change // res
                        nom.append(res_)
                        for x in range(1000000 - 1, 0, -1):
                            if len(nom) == 10:
                                break
                            elif len(nom) == n % 10 + 2:
                                break
                            
                            nom.append(x)
                            
                        #State of the program after the  for loop has been executed: `n` is an integer input from 11 to 105, `change` is 1000000, `nom` contains the integer 1, the integer division of 1000000 by `res`, and the appended value of `res_`, `x` is 0, the length of `nom` is either 11 or n % 10 + 4. If the length of `nom` is equal to 10, we break out of the loop. If the length of `nom` is equal to n % 10 + 2, the loop is exited.
                    #State of the program after the if block has been executed: *`n` is an integer input from 11 to 105, `change` is 1000000, `nom` contains the integer 1, the integer division of 1000000 by `res`, and the appended value of `res_`, `x` is 0, the length of `nom` is either 11 or n % 10 + 4. If the length of `nom` is equal to 10, we break out of the loop. If the length of `nom` is equal to n % 10 + 2, the loop is exited after the execution of the if statement.
                #State of the program after the if-else block has been executed: *`n` is an integer input from the standard input within the range of 11 to 105, `change` is 1000000, `nom` is a list containing integers. If 1000 < n <= 10000, `nom` contains integers with a length equal to the last digit of `n` plus 2. If n is not within the range of 11 to 100 and n is not between 100 and 1000, `nom` contains the integer 1, the integer division of 1000000 by `res`, and the appended value of `res_`, `x` is 0, the length of `nom` is either 11 or n % 10 + 4. If the length of `nom` is equal to 10, we break out of the loop. If the length of `nom` is equal to n % 10 + 2, the loop is exited after the execution of the if statement.
            #State of the program after the if-else block has been executed: *`n` is an integer from 11 to 105, `change` is 1000000, `nom` is a list containing integers. If 100 < n <= 1000, `nom` will contain 1 and a specific integer based on input `n` if n is less than 10, `nom` will have 10 elements starting from 1 to 10. If n is greater than or equal to 10, `nom` will have `n % 10 + 2` elements. If 1000 < n <= 10000, `nom` contains integers with a length equal to the last digit of `n` plus 2. If n is not within the range of 11 to 100 and n is not between 100 and 1000, `nom` contains the integer 1, the integer division of 1000000 by `res`, and the appended value of `res_`, `x` is 0, the length of `nom` is either 11 or n % 10 + 4. If the length of `nom` is equal to 10, we break out of the loop. If the length of `nom` is equal to n % 10 + 2, the loop is exited after the execution of the if statement.
        #State of the program after the if-else block has been executed: *`n` is an integer from 11 to 105, `change` is 1000000, `nom` is a list containing integers. If 10 < n <= 100, `nom` contains the integer 1 followed by the values of `res_`, `x` is 0, the length of `nom` is 10 or more. If 100 < n <= 1000, `nom` contains 1 and a specific integer based on input `n`. If n < 10, `nom` has 10 elements from 1 to 10. If n >= 10, `nom` has `n % 10 + 2` elements. If 1000 < n <= 10000, `nom` has integers with a length equal to the last digit of `n` plus 2. If n is not within the ranges mentioned, `nom` contains the integer 1, the integer division of 1000000 by `res`, the appended value of `res_`, `x` is 0, the length of `nom` is either 11 or n % 10 + 4. The loop is exited when the length of `nom` is 10 or n % 10 + 2 after the if statement is executed.
    #State of the program after the if-else block has been executed: *`n` is an integer input from 1 to 105, `change` is 1000000, `nom` is a list containing integers. If 1 <= n <= 10, `nom` contains integers 1000000 to 1000000 - `n` + 1 in descending order. If 10 < n <= 100, `nom` contains the integer 1 followed by the values of `res_`, `x` is 0, and the length of `nom` is 10 or more. If 100 < n <= 1000, `nom` contains 1 and a specific integer based on input `n`. If n < 10, `nom` has 10 elements from 1 to 10. If n >= 10, `nom` has `n % 10 + 2` elements. If 1000 < n <= 10000, `nom` has integers with a length equal to the last digit of `n` plus 2. If n is not within the mentioned ranges, `nom` contains the integer 1, the integer division of 1000000 by `res`, the appended value of `res_`, `x` is 0, and the length of `nom` is either 11 or n % 10 + 4. The loop is exited when the length of `nom` is 10 or n % 10 + 2 after the if-else block is executed.
    print(str(change) + ' ' + str(len(nom)))
    print(' '.join(list(map(str, nom))))
    exit(0)
#Overall this is what the function does:The function reads an integer input `n` from the standard input and constructs a list `nom` based on certain conditions. If `n` is between 1 and 10, `nom` contains integers in descending order from 1000000 to 1000000 - `n` + 1. If `n` is between 11 and 100, `nom` starts with 1 followed by specific values, and if `n` is between 101 and 1000, `nom` includes 1 and a specific integer based on `n`. For `n` between 1000 and 10000, `nom` is constructed with a length equal to the last digit of `n` plus 2. If `n` is 10000 or 100000, the function prints certain values and exits. The function then prints the change value and the length of `nom`, followed by the elements of `nom`. The function does not have a specific return value.


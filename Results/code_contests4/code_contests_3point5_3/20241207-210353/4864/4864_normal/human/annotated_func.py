#State of the program right berfore the function call: A is an integer such that 1 <= A <= 105.**
def func():
    n = int(sys.stdin.readline().rstrip('\n'))
    change = 1000000
    nom = [1]
    if (n <= 10) :
        for x in range(1000001 - 1, 0, -1):
            if len(nom) == n:
                break
            
            nom.append(x)
            
        #State of the program after the  for loop has been executed: Output State: A is an integer such that 1 <= A <= 105; n is an input integer read from standard input; change is 1000000; nom is a list containing the integers 1, 1000000, and all integers from 999999 down to 1000001-n. If n is greater than 999999, nom will contain all integers from 1 to 1000000.
    else :
        if (10 < n <= 100) :
            res = n - n % 10 - 1
            res_ = change // res
            nom.append(res_)
            for x in range(1000000 - 1, 0, -1):
                if len(nom) == 10:
                    break
                
                nom.append(x)
                
            #State of the program after the  for loop has been executed: A is an integer such that 1 <= A <= 105, n is an integer, change is 1000000, nom contains the integers 1 and values ranging from 999999 to 999991
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
                    
                #State of the program after the  for loop has been executed: `A` is an integer such that 1 <= A <= 105, `n` is an input integer read from standard input, `change` is 1000000, `nom` is a list containing the integer 1, the calculated value of `res_`, and integers from 999999 to 999990 in descending order
            else :
                if (1000 < n <= 10000) :
                    if (n == 10000) :
                        change = 10000
                        print(str(change) + ' ' + str(2))
                        print(str(1) + ' ' + str(9))
                        exit(0)
                    #State of the program after the if block has been executed: *A is an integer such that 1 <= A <= 105; n is an input integer read from standard input; change is 10000; nom is a list containing the integer 1. n is larger than 10. The value of n is either less than or equal to 10 or greater than 100. n is either less than or equal to 100 or greater than 1000. n is such that 1000 < n <= 10000. n is equal to 10000 and the code prints '10000 2'.
                    res = n - n % 10 - 1
                    res_ = change // res
                    nom.append(res_)
                    for x in range(1000000 - 1, 0, -1):
                        if len(nom) == 10:
                            break
                        elif len(nom) == n % 10 + 2:
                            break
                        
                        nom.append(x)
                        
                    #State of the program after the  for loop has been executed: `A` is an integer between 1 and 105, `n` is equal to 10000, `change` is 10000, `nom` is a list containing integers starting from 1 and adding consecutive integers until n % 10 + 2 is reached, `res` is 9999, `res_` is 1
                else :
                    if (10000 < n <= 100000) :
                        if (n == 100000) :
                            change = 100000
                            print(str(change) + ' ' + str(2))
                            print(str(1) + ' ' + str(9))
                            exit(0)
                        #State of the program after the if block has been executed: *`A` is an integer such that 1 <= A <= 105; `n` is an input integer read from standard input; `change` is 100000; `nom` is a list containing the integer 1; n is larger than 10. The value of n is either less than or equal to 10 or greater than 100. n is either less than or equal to 100 or greater than 1000. n is either less than or equal to 1000 or greater than 10000. n is such that 10000 < n <= 100000. If n == 100000, the program prints '100000 2' as the output.
                        res = n - n % 10 - 1
                        res_ = change // res
                        nom.append(res_)
                        for x in range(1000000 - 1, 0, -1):
                            if len(nom) == 10:
                                break
                            elif len(nom) == n % 10 + 2:
                                break
                            
                            nom.append(x)
                            
                        #State of the program after the  for loop has been executed: `A` is an integer such that 1 <= A <= 105, `n` is an input integer greater than 0, `change` is 100000, `nom` contains the integer 1 and additional values based on the calculation of `res_`
                    #State of the program after the if block has been executed: *A is an integer such that 1 <= A <= 105, n is an input integer greater than 0, change is 1000000, nom contains the integer 1 and additional values based on the calculation of res_.
                #State of the program after the if-else block has been executed: *`A` is an integer between 1 and 105. If 1000 < n <= 10000, then `n` is equal to 10000, `change` is 10000, `nom` is a list containing integers starting from 1 and adding consecutive integers until n % 10 + 2 is reached, `res` is 9999, `res_` is 1. If the condition is not met, then `A` is an integer between 1 and 105, `n` is an input integer greater than 0, `change` is 1000000, `nom` contains the integer 1 and additional values based on the calculation of res_.
            #State of the program after the if-else block has been executed: *`A` is an integer between 1 and 105, `n` is an input integer, `change` is either 1000000 or 10000, `nom` is a list containing the integer 1 and additional values based on the calculation of `res_`, `res_` is either 1 or a value based on the conditions of the if else block. If 100 < n <= 1000, then `n` is an input integer, `change` is 1000000, and `nom` contains integers from 999999 to 999990 in descending order. If 1000 < n <= 10000, then `n` is 10000, `change` is 10000, `nom` contains integers starting from 1 and adding consecutive integers until n % 10 + 2, `res` is 9999, and `res_` is 1.
        #State of the program after the if-else block has been executed: *A is an integer such that 1 <= A <= 105, n is an input integer, change is either 1000000 or 10000, nom is a list containing the integer 1 and other integers based on the conditions of the if else block. If 10 < n <= 100, nom contains integers ranging from 999999 to 999991. If 100 < n <= 1000, nom contains integers from 999999 to 999990 in descending order. If 1000 < n <= 10000, nom starts from 1 and increases by consecutive integers until n % 10 + 2. res is 9999 if n is between 1000 and 10000, otherwise res is 1.
    #State of the program after the if-else block has been executed: *A is an integer such that 1 <= A <= 105; n is an input integer; change is either 1000000 or 10000; nom is a list containing the integers based on the conditions of the if else block. If n <= 10, nom contains 1, 1000000, and all integers from 999999 down to 1000001-n. If n is greater than 999999, nom will contain all integers from 1 to 1000000. If 10 < n <= 100, nom contains integers ranging from 999999 to 999991. If 100 < n <= 1000, nom contains integers from 999999 to 999990 in descending order. If 1000 < n <= 10000, nom starts from 1 and increases by consecutive integers until n % 10 + 2. res is 9999 if n is between 1000 and 10000, otherwise res is 1.
    print(str(change) + ' ' + str(len(nom)))
    print(' '.join(list(map(str, nom))))
    exit(0)
#Overall this is what the function does:The function `func` reads an integer input from the standard input, calculates a list of integers based on the input value, and prints the list along with other information. The function handles different cases based on the input value, such as when the input is less than or equal to 10, between 10 and 100, between 100 and 1000, between 1000 and 10000, and greater than 10000. In each case, it adjusts the list of integers accordingly. However, despite the annotations mentioning different scenarios, the actual code only prints out the list without returning any value. Also, there are missing edge cases such as when the input value is greater than 100000.


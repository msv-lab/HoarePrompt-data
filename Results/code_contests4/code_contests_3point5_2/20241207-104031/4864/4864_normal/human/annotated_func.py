#State of the program right berfore the function call: A is an integer such that 1 ≤ A ≤ 105.**
def func():
    n = int(sys.stdin.readline().rstrip('\n'))
    change = 1000000
    nom = [1]
    if (n <= 10) :
        for x in range(1000001 - 1, 0, -1):
            if len(nom) == n:
                break
            
            nom.append(x)
            
        #State of the program after the  for loop has been executed: `A` is an integer such that 1 ≤ `A` ≤ 105, `n` is the integer input from standard input, `change` is 1000000, `nom` is a list containing 1 and numbers from 1000000 down to 1000000 - `n` + 1 (inclusive), `n` is less than or equal to 10.
    else :
        if (10 < n <= 100) :
            res = n - n % 10 - 1
            res_ = change // res
            nom.append(res_)
            for x in range(1000000 - 1, 0, -1):
                if len(nom) == 10:
                    break
                
                nom.append(x)
                
            #State of the program after the  for loop has been executed: A is an integer such that 1 ≤ A ≤ 105, n is the integer input from standard input, change is 1000000, nom is a list containing 999989 elements, the result of 1000000 divided by res
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
                    
                #State of the program after the  for loop has been executed: At the end of the loop execution, `A` is an integer such that 1 ≤ A ≤ 105, `n` is the integer input, `change` is 1000000, `nom` is a list containing 1, the calculated `res_` value, 999999, and the remaining elements added by the loop until the length of `nom` is equal to 10 or `n % 10 + 2`. If the loop does not execute, `nom` will contain only 1 and the calculated `res_` value.
            else :
                if (1000 < n <= 10000) :
                    if (n == 10000) :
                        change = 10000
                        print(str(change) + ' ' + str(2))
                        print(str(1) + ' ' + str(9))
                        exit(0)
                    #State of the program after the if block has been executed: *A is an integer such that 1 ≤ A ≤ 105; n is the integer input from standard input; change is 10000; nom is a list containing 1; if n == 10000, the output of the print statement is '1 9'.
                    res = n - n % 10 - 1
                    res_ = change // res
                    nom.append(res_)
                    for x in range(1000000 - 1, 0, -1):
                        if len(nom) == 10:
                            break
                        elif len(nom) == n % 10 + 2:
                            break
                        
                        nom.append(x)
                        
                    #State of the program after the  for loop has been executed: `A` is an integer such that 1 ≤ A ≤ 105, `n` is the integer input from standard input, `change` is 10000, `nom` is a list containing elements 1, 1, 999998, 999997, 999996, 999995, 999994, 999993, 999992, 999991, 999990, `res` is 9999, `res_` is 1
                else :
                    if (10000 < n <= 100000) :
                        if (n == 100000) :
                            change = 100000
                            print(str(change) + ' ' + str(2))
                            print(str(1) + ' ' + str(9))
                            exit(0)
                        #State of the program after the if block has been executed: *A is an integer such that 1 ≤ A ≤ 105; n is the integer input from standard input; change is 1000000; nom is a list containing 1. If n == 100000, the program exits with status code 0.
                        res = n - n % 10 - 1
                        res_ = change // res
                        nom.append(res_)
                        for x in range(1000000 - 1, 0, -1):
                            if len(nom) == 10:
                                break
                            elif len(nom) == n % 10 + 2:
                                break
                            
                            nom.append(x)
                            
                        #State of the program after the  for loop has been executed: `A` is an integer such that 1 ≤ A ≤ 105, `n` is the integer input from standard input, `change` is 999999, `nom` is a list containing values of x appended in the loop until the length becomes 10 or is updated to n % 10 + 2 based on the condition. If the length of `nom` becomes 10, we break out of the most internal loop or if statement.
                    #State of the program after the if block has been executed: *`A` is an integer such that 1 ≤ A ≤ 105, `n` is the integer input from standard input, `change` is 1000000, `nom` is a list containing values of x appended in the loop until the length becomes 10 or is updated to n % 10 + 2 based on the condition. If the length of `nom` becomes 10, we break out of the most internal loop or if statement.
                #State of the program after the if-else block has been executed: *`A` is an integer such that 1 ≤ A ≤ 105, `n` is the integer input from standard input, `change` is either 10000 or 1000000 based on the value of `n`, `nom` is a list containing elements based on the conditions specified in the if and else parts. If 1000 < n <= 10000, `nom` will contain 1, 1, 999998, 999997, 999996, 999995, 999994, 999993, 999992, 999991, 999990. If n is not in the range (10 < n <= 100), `nom` will contain values of x appended in the loop until the length becomes 10 or is updated to n % 10 + 2 based on the condition. If the length of `nom` becomes 10, we break out of the most internal loop or if statement.
            #State of the program after the if-else block has been executed: *`A` is an integer such that 1 ≤ A ≤ 105, `n` is the integer input, `change` is either 10000 or 1000000 based on the value of `n`, `nom` is a list containing elements based on the conditions specified in the if and else parts. If 100 < n ≤ 1000, `nom` will contain 1, 1, 999998, 999997, 999996, 999995, 999994, 999993, 999992, 999991, 999990, the calculated `res_` value, 999999, and the remaining elements added by the loop until the length of `nom` is equal to 10 or `n % 10 + 2`. If 1000 < n ≤ 10000, `nom` will contain 1, 1, 999998, 999997, 999996, 999995, 999994, 999993, 999992, 999991, 999990. If n is not in the range (10 < n ≤ 100), `nom` will contain values of x appended in the loop until the length becomes 10 or is updated to n % 10 + 2 based on the condition. If the length of `nom` becomes 10, we break out of the most internal loop or if statement.
        #State of the program after the if-else block has been executed: *`A` is an integer such that 1 ≤ A ≤ 105, `n` is the integer input, `change` is either 10000 or 1000000 based on the value of `n`, `nom` is a list containing elements based on the conditions specified in the if and else parts. If 10 < n ≤ 100, `nom` will contain 999989 elements and the result of 1000000 divided by res. If 100 < n ≤ 1000, `nom` will contain 1, 1, 999998, 999997, 999996, 999995, 999994, 999993, 999992, 999991, 999990. If 1000 < n ≤ 10000, `nom` will contain 1, 1, 999998, 999997, 999996, 999995, 999994, 999993, 999992, 999991, 999990. If n is not in the range (10 < n ≤ 100), `nom` will contain values of x appended in the loop until the length becomes 10 or is updated to n % 10 + 2 based on the condition. If the length of `nom` becomes 10, we break out of the most internal loop or if statement.
    #State of the program after the if-else block has been executed: *`A` is an integer such that 1 ≤ `A` ≤ 105, `n` is the integer input, `change` is either 10000 or 1000000 based on the value of `n`, `nom` is a list containing elements based on the conditions specified in the if and else parts. If 10 < n ≤ 100, `nom` will contain 999989 elements and the result of 1000000 divided by res. If 100 < n ≤ 1000, `nom` will contain 1, 1, 999998, 999997, 999996, 999995, 999994, 999993, 999992, 999991, 999990. If 1000 < n ≤ 10000, `nom` will contain 1, 1, 999998, 999997, 999996, 999995, 999994, 999993, 999992, 999991, 999990. If n is not in the range (10 < n ≤ 100), `nom` will contain values of x appended in the loop until the length becomes 10 or is updated to n % 10 + 2 based on the condition. If the length of `nom` becomes 10, we break out of the most internal loop or if statement.
    print(str(change) + ' ' + str(len(nom)))
    print(' '.join(list(map(str, nom))))
    exit(0)
#Overall this is what the function does:The function `func` reads an integer input from standard input, and based on the value of the input, it constructs a list `nom` with specific elements. The function then prints out the values of `change` and the length of `nom`, followed by the elements of `nom` separated by spaces. The function operates without any explicit input parameters and is designed to handle different input ranges of `n` to generate the list `nom` accordingly. If `n` falls within specific ranges, the function constructs `nom` with predetermined elements. If `n` is not within the predefined ranges, the function appends elements to `nom` until its length reaches 10 or `n % 10 + 2`. The program then exits with status code 0.


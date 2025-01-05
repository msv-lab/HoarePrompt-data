#State of the program right berfore the function call: A is a single integer such that 1 ≤ A ≤ 10^5.
def func():
    n = int(sys.stdin.readline().rstrip('\n'))
    change = 1000000
    nom = [1]
    if (n <= 10) :
        for x in range(1000001 - 1, 0, -1):
            if len(nom) == n:
                break
            
            nom.append(x)
            
        #State of the program after the  for loop has been executed: `A` is a single integer such that 1 ≤ `A` ≤ 10^5, `n` is an input integer within that range and `n` is less than or equal to 10; `nom` contains the values [1, 1000000, 999999, 999998, 999997, 999996, 999995, 999994, 999993, 999992] if `n` is 10, and if `n` is less than 10, `nom` contains the values [1, 1000000, 999999, ..., 1000000 - (n - 1)].
    else :
        if (10 < n <= 100) :
            res = n - n % 10 - 1
            res_ = change // res
            nom.append(res_)
            for x in range(1000000 - 1, 0, -1):
                if len(nom) == 10:
                    break
                
                nom.append(x)
                
            #State of the program after the  for loop has been executed: `A` is a single integer such that 1 ≤ A ≤ 10^5; `n` is an input integer (11 ≤ n ≤ 100); `change` is 1000000; `nom` is a list of integers containing 10 elements; `res` is between 10 and 99; `res_` is between 10101 and 100000.
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
                    
                #State of the program after the  for loop has been executed: `A` is a single integer such that 1 ≤ A ≤ 10^5, `n` is an integer larger than 100 and within the range of 100 to 1000, `change` is 1000000, `nom` has at most 11 elements with the last element being either 999990 or 999989 depending on the break condition, `res` is between 98 and 999, `res_` is between 1000 and 10101.
            else :
                if (1000 < n <= 10000) :
                    if (n == 10000) :
                        change = 10000
                        print(str(change) + ' ' + str(2))
                        print(str(1) + ' ' + str(9))
                        exit(0)
                    #State of the program after the if block has been executed: *`A` is a single integer such that 1 ≤ A ≤ 10^5; `n` is equal to 10000, so `change` is set to 10000, `nom` remains as [1], and the output is "10000 2", with a printed output of "1 9".
                    res = n - n % 10 - 1
                    res_ = change // res
                    nom.append(res_)
                    for x in range(1000000 - 1, 0, -1):
                        if len(nom) == 10:
                            break
                        elif len(nom) == n % 10 + 2:
                            break
                        
                        nom.append(x)
                        
                    #State of the program after the  for loop has been executed: `A` is a single integer such that 1 ≤ `A` ≤ 10^5, `n` is 10000, `change` is 10000, `nom` is a list containing 2 elements, the output is "10000 2", printed output is "1 9", `res` is 9999, `res_` is 1, `x` is 999999.
                else :
                    if (10000 < n <= 100000) :
                        if (n == 100000) :
                            change = 100000
                            print(str(change) + ' ' + str(2))
                            print(str(1) + ' ' + str(9))
                            exit(0)
                        #State of the program after the if block has been executed: *`A` is a single integer such that 1 ≤ `A` ≤ 10^5; `n` is an input integer larger than 100 and within the specified ranges; `change` is 1000000; `nom` is [1]; if `n` is equal to 100000, the output is "100000 2", printed output is "1 9", and the program exits.
                        res = n - n % 10 - 1
                        res_ = change // res
                        nom.append(res_)
                        for x in range(1000000 - 1, 0, -1):
                            if len(nom) == 10:
                                break
                            elif len(nom) == n % 10 + 2:
                                break
                            
                            nom.append(x)
                            
                        #State of the program after the  for loop has been executed: `A` is a single integer such that 1 ≤ `A` ≤ 10^5, `n` is 100000, `change` is 1000000, `nom` contains 10 elements, `res` is 99999, `res_` is 10, and `x` is 999992.
                    #State of the program after the if block has been executed: *`A` is a single integer such that 1 ≤ `A` ≤ 10^5, `n` is an integer greater than 100. If 10000 < `n` ≤ 100000, then `n` is set to 100000, `change` is 1000000, `nom` contains 10 elements, `res` is 99999, `res_` is 10, and `x` is 999992.
                #State of the program after the if-else block has been executed: *`A` is a single integer such that 1 ≤ `A` ≤ 10^5. If `n` is 10000, `change` is updated to 10000, `nom` becomes a list containing 2 elements, the output is "10000 2", printed output is "1 9", `res` is 9999, `res_` is 1, and `x` is 999999. Otherwise, if `n` is greater than 100 but less than or equal to 100000, then if 10000 < `n` ≤ 100000, `n` is set to 100000, `change` remains 1000000, `nom` contains 10 elements, `res` is 99999, `res_` is 10, and `x` is 999992.
            #State of the program after the if-else block has been executed: *`A` is a single integer such that 1 ≤ `A` ≤ 10^5. If `n` is an integer larger than 100 and within the range of 100 to 1000, `change` is 1000000, `nom` has at most 11 elements with the last element being either 999990 or 999989 depending on the break condition, `res` is between 98 and 999, and `res_` is between 1000 and 10101. Otherwise, if `n` is 10000, `change` is updated to 10000, `nom` becomes a list containing 2 elements, the output is "10000 2", printed output is "1 9", `res` is 9999, `res_` is 1, and `x` is 999999. If `n` is greater than 100 but less than or equal to 100000, and if 10000 < `n` ≤ 100000, then `n` is set to 100000, `change` remains 1000000, `nom` contains 10 elements, `res` is 99999, `res_` is 10, and `x` is 999992.
        #State of the program after the if-else block has been executed: *`A` is a single integer such that 1 ≤ `A` ≤ 10^5. If `n` is an integer within the range of 11 to 100, then `change` is 1000000, `nom` is a list of integers containing 10 elements, `res` is between 10 and 99, and `res_` is between 10101 and 100000. If `n` is larger than 100 and within the range of 101 to 1000, then `change` is 1000000, `nom` has at most 11 elements with the last element being either 999990 or 999989 depending on the break condition, `res` is between 98 and 999, and `res_` is between 1000 and 10101. If `n` is exactly 10000, then `change` is updated to 10000, `nom` becomes a list containing 2 elements, the output is "10000 2", printed output is "1 9", `res` is 9999, `res_` is 1, and `x` is 999999. If `n` is greater than 100 but less than or equal to 100000, and if 10000 < `n` ≤ 100000, then `n` is set to 100000, `change` remains 1000000, `nom` contains 10 elements, `res` is 99999, `res_` is 10, and `x` is 999992.
    #State of the program after the if-else block has been executed: *`A` is a single integer such that 1 ≤ `A` ≤ 10^5. If `n` is less than or equal to 10, then `nom` contains the values [1, 1000000, 999999, 999998, 999997, 999996, 999995, 999994, 999993, 999992] if `n` is 10, otherwise `nom` contains the values [1, 1000000, 999999, ..., 1000000 - (n - 1)]. If `n` is between 11 and 100, then `change` is 1000000, `nom` is a list of integers containing 10 elements, `res` is between 10 and 99, and `res_` is between 10101 and 100000. If `n` is between 101 and 1000, `change` remains 1000000, `nom` has at most 11 elements with the last element being either 999990 or 999989, `res` is between 98 and 999, and `res_` is between 1000 and 10101. If `n` is exactly 10000, then `change` is updated to 10000, `nom` contains 2 elements, the output is "10000 2", printed output is "1 9", `res` is 9999, `res_` is 1, and `x` is 999999. If `n` is greater than 100 but less than or equal to 100000, and if 10000 < `n` ≤ 100000, then `n` is set to 100000, `change` remains 1000000, `nom` contains 10 elements, `res` is 99999, `res_` is 10, and `x` is 999992.
    print(str(change) + ' ' + str(len(nom)))
    print(' '.join(list(map(str, nom))))
    exit(0)
#Overall this is what the function does:The function reads an integer `n` from input, which is constrained to the range 1 ≤ n ≤ 100,000. Depending on the value of `n`, the function generates a list `nom` and outputs its length and contents. If `n` is 10 or less, `nom` will contain the integers from 1 to 1,000,000 down to a certain value. If `n` is between 11 and 100, `nom` will include a calculated value based on `n` and then fill up to 10 elements. For `n` between 101 and 1000, it behaves similarly but with additional break conditions based on the length of `nom`. If `n` equals 10,000 or 100,000, the function will print specific output and exit. The function does not return a value but prints the result directly. It also handles edge cases for input values at the boundaries of the defined ranges.


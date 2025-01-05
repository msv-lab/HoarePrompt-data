#State of the program right berfore the function call: A is an integer such that 1 ≤ A ≤ 10^5.
def func():
    n = int(sys.stdin.readline().rstrip('\n'))
    change = 1000000
    nom = [1]
    if (n <= 10) :
        for x in range(1000001 - 1, 0, -1):
            if len(nom) == n:
                break
            
            nom.append(x)
            
        #State of the program after the  for loop has been executed: `A` is an integer such that 1 ≤ `A` ≤ 10^5; `n` is an integer input less than or equal to 10; `change` is 1000000; `nom` is a list containing `n` elements starting from `1` to `1000001 - n`; `x` is `1000001 - n`; the length of `nom` is equal to `n`.
    else :
        if (10 < n <= 100) :
            res = n - n % 10 - 1
            res_ = change // res
            nom.append(res_)
            for x in range(1000000 - 1, 0, -1):
                if len(nom) == 10:
                    break
                
                nom.append(x)
                
            #State of the program after the  for loop has been executed: `A` is an integer such that 1 ≤ `A` ≤ 10^5; `n` is an integer larger than 10 and less than or equal to 100; `change` is 1000000; `nom` is a list containing 10 elements [1, res_, 999999, 999998, 999997, 999996, 999995, 999994, 999993, 999992]; `res` is an integer between 9 and 99; `res_` is an integer between 10101 and 111111.
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
                    
                #State of the program after the  for loop has been executed: `A` is an integer such that 1 ≤ `A` ≤ 10^5; `n` is an integer larger than 100 and satisfies 100 < `n` ≤ 1000; `change` is 1000000; `nom` is a list with 10 elements, starting with [1, `res_`] followed by the next 8 decremented values from 999999 down to a value that maintains the length of `nom` at 10; `x` is 999990.
            else :
                if (1000 < n <= 10000) :
                    if (n == 10000) :
                        change = 10000
                        print(str(change) + ' ' + str(2))
                        print(str(1) + ' ' + str(9))
                        exit(0)
                    #State of the program after the if block has been executed: *`A` is an integer such that 1 ≤ `A` ≤ 10^5; `n` is an integer equal to 10000; `change` is 10000; `nom` is [1]; and the printed output is "1 9".
                    res = n - n % 10 - 1
                    res_ = change // res
                    nom.append(res_)
                    for x in range(1000000 - 1, 0, -1):
                        if len(nom) == 10:
                            break
                        elif len(nom) == n % 10 + 2:
                            break
                        
                        nom.append(x)
                        
                    #State of the program after the  for loop has been executed: `A` is an integer such that 1 ≤ `A` ≤ 10^5; `n` is 10000; `change` is 10000; `nom` is [1, 1]; `res` is 9999; `res_` is 1; printed output is "1 9".
                else :
                    if (10000 < n <= 100000) :
                        if (n == 100000) :
                            change = 100000
                            print(str(change) + ' ' + str(2))
                            print(str(1) + ' ' + str(9))
                            exit(0)
                        #State of the program after the if block has been executed: *`A` is an integer such that 1 ≤ `A` ≤ 10^5, `n` is 100000, `change` is 1000000, and `nom` is [1]. The program execution is terminated with exit(0) if `n` equals 100000.
                        res = n - n % 10 - 1
                        res_ = change // res
                        nom.append(res_)
                        for x in range(1000000 - 1, 0, -1):
                            if len(nom) == 10:
                                break
                            elif len(nom) == n % 10 + 2:
                                break
                            
                            nom.append(x)
                            
                        #State of the program after the  for loop has been executed: `A` is an integer such that 1 ≤ `A` ≤ 10^5, `n` is 100000, `change` is 1000000, `nom` is a list containing 10 elements, `res` is 99999, `res_` is 10, `x` is 999992.
                    #State of the program after the if block has been executed: *`A` is an integer such that 1 ≤ `A` ≤ 10^5, `n` is larger than 100 and not less than or equal to 1000, `change` is 1000000, `nom` is a list containing 1 element, and if `n` is greater than 10000 and less than or equal to 100000, then `n` is 100000, `res` is 99999, `res_` is 10, and `x` is 999992.
                #State of the program after the if-else block has been executed: *`A` is an integer such that 1 ≤ `A` ≤ 10^5; if `n` is between 1000 and 10000 (inclusive), then `n` is set to 10000, `change` is set to 10000, `nom` becomes [1, 1], `res` is 9999, `res_` is 1, and the printed output is "1 9". Otherwise, if `n` is greater than 10000 and less than or equal to 100000, then `n` is set to 100000, `res` is 99999, `res_` is 10, and `x` is 999992; meanwhile, `change` remains 1000000 and `nom` is a list containing 1 element.
            #State of the program after the if-else block has been executed: *`A` is an integer such that 1 ≤ `A` ≤ 10^5; if `n` is an integer larger than 100 and satisfies 100 < `n` ≤ 1000, then `change` is 1000000, `nom` is a list with 10 elements starting with [1, `res_`] followed by the next 8 decremented values from 999999 down to a value that maintains the length of `nom` at 10, and `x` is 999990. Otherwise, if `n` is between 1000 and 10000 (inclusive), then `n` is set to 10000, `change` is set to 10000, `nom` becomes [1, 1], `res` is 9999, `res_` is 1, and the printed output is "1 9". If `n` is greater than 10000 and less than or equal to 100000, then `n` is set to 100000, `res` is 99999, `res_` is 10, `x` is 999992, and `change` remains 1000000 with `nom` being a list containing 1 element.
        #State of the program after the if-else block has been executed: *`A` is an integer such that 1 ≤ `A` ≤ 10^5; if `n` is an integer larger than 10 and less than or equal to 100, then `change` is 1000000, `nom` is a list containing 10 elements [1, `res_`, 999999, 999998, 999997, 999996, 999995, 999994, 999993, 999992], where `res` is an integer between 9 and 99 and `res_` is an integer between 10101 and 111111. Otherwise, if `n` is larger than 100 and less than or equal to 1000, then `change` is 1000000, `nom` is a list starting with [1, `res_`] followed by the next 8 decremented values from 999999 down to a value that maintains the length of `nom` at 10, and `x` is 999990. If `n` is between 1000 and 10000 (inclusive), then `n` is set to 10000, `change` is set to 10000, `nom` becomes [1, 1], `res` is 9999, `res_` is 1, and the printed output is "1 9". If `n` is greater than 10000 and less than or equal to 100000, then `n` is set to 100000, `res` is 99999, `res_` is 10, `x` is 999992, and `change` remains 1000000 with `nom` being a list containing 1 element.
    #State of the program after the if-else block has been executed: *`A` is an integer such that 1 ≤ `A` ≤ 10^5; if `n` is an integer less than or equal to 10, `change` is set to 1000000, `nom` is a list containing `n` elements starting from `1` to `1000001 - n`, and `x` is `1000001 - n`. If `n` is larger than 10 and less than or equal to 100, `change` remains 1000000, `nom` is a list containing 10 elements [1, `res_`, 999999, 999998, 999997, 999996, 999995, 999994, 999993, 999992], with `res` between 9 and 99 and `res_` between 10101 and 111111. If `n` is larger than 100 and less than or equal to 1000, `change` is still 1000000, `nom` starts with [1, `res_`] followed by the next 8 decremented values from 999999 down to ensure the length of `nom` is 10, and `x` is 999990. For `n` between 1000 and 10000 (inclusive), `n` is set to 10000, `change` is set to 10000, `nom` becomes [1, 1], `res` is 9999, `res_` is 1, and the printed output is "1 9". Finally, if `n` is greater than 10000 and less than or equal to 100000, `n` is set to 100000, `res` is 99999, `res_` is 10, `x` is 999992, and `change` remains 1000000 with `nom` being a list containing 1 element.
    print(str(change) + ' ' + str(len(nom)))
    print(' '.join(list(map(str, nom))))
    exit(0)
#Overall this is what the function does:The function reads an integer input `n` from standard input and generates a list `nom` based on the value of `n`. If `n` is between 1 and 10, it adds numbers from 1 to `1000001 - n` to `nom`. If `n` is between 11 and 100, it computes a value `res_` based on `n` and adds it along with values from `999999` down to ensure `nom` has 10 elements. For `n` between 101 and 1000, it behaves similarly, ensuring the length of `nom` remains 10. If `n` is between 1001 and 10000, it prints "1 9" and terminates. If `n` is 10000 or 100000, it prints "10000 2" or "100000 2" respectively and also prints "1 9" before terminating. The output includes the value of `change` and the length of `nom`, followed by the elements of `nom`. The function does not return anything but prints results to standard output.


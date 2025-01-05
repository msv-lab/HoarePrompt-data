#State of the program right berfore the function call: A is a single integer such that 1 ≤ A ≤ 10^5. The output consists of two integers N and M (1 ≤ N ≤ 10^6, 1 ≤ M ≤ 10), followed by M distinct integers D1, D2, ..., DM (1 ≤ Di ≤ 10^6).
def func():
    n = int(sys.stdin.readline().rstrip('\n'))
    change = 1000000
    nom = [1]
    if (n <= 10) :
        for x in range(1000001 - 1, 0, -1):
            if len(nom) == n:
                break
            
            nom.append(x)
            
        #State of the program after the  for loop has been executed: `A` is a single integer such that 1 ≤ `A` ≤ 10^5, `n` is less than or equal to 10, `change` is 1000000, `nom` is a list containing the integers starting from 1 down to (1,000,001 - n), and `x` will be less than or equal to 999,999.
    else :
        if (10 < n <= 100) :
            res = n - n % 10 - 1
            res_ = change // res
            nom.append(res_)
            for x in range(1000000 - 1, 0, -1):
                if len(nom) == 10:
                    break
                
                nom.append(x)
                
            #State of the program after the  for loop has been executed: `A` is a single integer such that 1 ≤ `A` ≤ 10^5, `n` is an integer greater than 10 and less than or equal to 100, `change` is 1000000, `nom` is a list containing the integers 1, `res_`, and the 8 largest integers from 999999 down to 999992, `res` is calculated as `n - n % 10 - 1`, `res_` is calculated as `1000000 // res`.
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
                    
                #State of the program after the  for loop has been executed: `A` is a single integer such that 1 ≤ `A` ≤ 10^5; `n` is greater than 100 and less than or equal to 1000; `change` is 1000000; `nom` has 10 elements; `res` is `n - n % 10 - 1`; `res_` is between approximately 1001 and 10989.
            else :
                if (1000 < n <= 10000) :
                    if (n == 10000) :
                        change = 10000
                        print(str(change) + ' ' + str(2))
                        print(str(1) + ' ' + str(9))
                        exit(0)
                    #State of the program after the if block has been executed: *`A` is a single integer such that 1 ≤ `A` ≤ 10^5; `n` is 10000; `change` is 10000; `nom` is [1]; the printed output is '10000 2' and the program terminates. If `n` is not equal to 10000, the program does not execute any specific actions as there is no else part defined.
                    res = n - n % 10 - 1
                    res_ = change // res
                    nom.append(res_)
                    for x in range(1000000 - 1, 0, -1):
                        if len(nom) == 10:
                            break
                        elif len(nom) == n % 10 + 2:
                            break
                        
                        nom.append(x)
                        
                    #State of the program after the  for loop has been executed: `A` is a single integer such that 1 ≤ `A` ≤ 10^5, `n` is 10000, `change` is 10000, `nom` is [1, 1, 999999, 999998, 999997, 999996, 999995, 999994, 999993, 999992], the printed output is '10000 2', `res` is 9999, `res_` is 1, `x` is 999992.
                else :
                    if (10000 < n <= 100000) :
                        if (n == 100000) :
                            change = 100000
                            print(str(change) + ' ' + str(2))
                            print(str(1) + ' ' + str(9))
                            exit(0)
                        #State of the program after the if block has been executed: *`A` is a single integer such that 1 ≤ `A` ≤ 10^5; `n` is equal to 100000; `change` is 100000; `nom` is [1]; the output of the print statement is "1 9", and the program has exited.
                        res = n - n % 10 - 1
                        res_ = change // res
                        nom.append(res_)
                        for x in range(1000000 - 1, 0, -1):
                            if len(nom) == 10:
                                break
                            elif len(nom) == n % 10 + 2:
                                break
                            
                            nom.append(x)
                            
                        #State of the program after the  for loop has been executed: `A` is a single integer such that 1 ≤ `A` ≤ 10^5, `n` is 100000, `change` is 100000, `nom` contains 2 elements, the output of the print statement is "1 9", `res` is 99999, `res_` is 1.
                    #State of the program after the if block has been executed: *`A` is a single integer such that 1 ≤ `A` ≤ 10^5, if `n` is between 10001 and 100000 inclusive, then `n` is set to 100000, `change` is updated to 100000, `nom` contains 2 elements, the output of the print statement is "1 9", `res` is 99999, and `res_` is 1. Otherwise, no changes occur.
                #State of the program after the if-else block has been executed: *`A` is a single integer such that 1 ≤ `A` ≤ 10^5. If `n` is between 1000 and 10000 inclusive, then `n` is 10000, `change` is 10000, `nom` becomes [1, 1, 999999, 999998, 999997, 999996, 999995, 999994, 999993, 999992], the printed output is '10000 2', `res` is 9999, `res_` is 1, and `x` is 999992. If `n` is between 10001 and 100000 inclusive, then `n` is set to 100000, `change` is updated to 100000, `nom` contains 2 elements, the output is "1 9", `res` is 99999, and `res_` is 1. Otherwise, no changes occur.
            #State of the program after the if-else block has been executed: *`A` is a single integer such that 1 ≤ `A` ≤ 10^5. If `n` is greater than 100 and less than or equal to 1000, `change` remains 1000000, `nom` has 10 elements, `res` is calculated as `n - n % 10 - 1`, and `res_` is between approximately 1001 and 10989. If `n` is between 1000 and 10000 inclusive, then `n` is set to 10000, `change` is 10000, `nom` becomes [1, 1, 999999, 999998, 999997, 999996, 999995, 999994, 999993, 999992], the printed output is '10000 2', `res` is 9999, `res_` is 1, and `x` is 999992. If `n` is between 10001 and 100000 inclusive, then `n` is set to 100000, `change` is updated to 100000, `nom` contains 2 elements, the output is "1 9", `res` is 99999, and `res_` is 1. Otherwise, no changes occur.
        #State of the program after the if-else block has been executed: *`A` is a single integer such that 1 ≤ `A` ≤ 10^5. If `n` is greater than 10 and less than or equal to 100, `change` is 1000000, `nom` is a list containing the integers 1, `res_`, and the 8 largest integers from 999999 down to 999992, `res` is calculated as `n - n % 10 - 1`, and `res_` is calculated as `1000000 // res`. If `n` is greater than 100 and less than or equal to 1000, `change` remains 1000000, `nom` has 10 elements, and `res` is calculated as `n - n % 10 - 1` with `res_` between approximately 1001 and 10989. If `n` is between 1000 and 10000 inclusive, `n` is set to 10000, `change` is 10000, `nom` becomes [1, 1, 999999, 999998, 999997, 999996, 999995, 999994, 999993, 999992], the printed output is '10000 2', `res` is 9999, `res_` is 1, and `x` is 999992. If `n` is between 10001 and 100000 inclusive, then `n` is set to 100000, `change` is updated to 100000, `nom` contains 2 elements, the output is "1 9", `res` is 99999, and `res_` is 1. Otherwise, no changes occur.
    #State of the program after the if-else block has been executed: *`A` is a single integer such that 1 ≤ `A` ≤ 10^5. If `n` is less than or equal to 10, `change` is 1000000, and `nom` is a list containing the integers from 1 to (1,000,001 - n). If `n` is greater than 10 and less than or equal to 100, `change` is 1000000, `nom` contains the integers 1, `res_`, and the 8 largest integers from 999999 down to 999992, where `res` is calculated as `n - n % 10 - 1` and `res_` is calculated as `1000000 // res`. If `n` is greater than 100 and less than or equal to 1000, `change` remains 1000000, `nom` has 10 elements, and `res` is calculated as `n - n % 10 - 1` with `res_` between approximately 1001 and 10989. If `n` is between 1000 and 10000 inclusive, `n` is set to 10000, `change` is 10000, `nom` becomes [1, 1, 999999, 999998, 999997, 999996, 999995, 999994, 999993, 999992], the printed output is '10000 2', `res` is 9999, `res_` is 1, and `x` is 999992. If `n` is between 10001 and 100000 inclusive, then `n` is set to 100000, `change` is updated to 100000, `nom` contains 2 elements, the output is "1 9", `res` is 99999, and `res_` is 1. Otherwise, no changes occur.
    print(str(change) + ' ' + str(len(nom)))
    print(' '.join(list(map(str, nom))))
    exit(0)
#Overall this is what the function does:The function reads an integer `n` from input and generates a list of integers based on the value of `n`. If `n` is between 1 and 10, it creates a list of the first `n` integers in descending order. If `n` is between 11 and 100, it appends a calculated value based on `n` and then fills the list with the largest integers down to 1 until the list has 10 elements. If `n` is between 101 and 1000, it performs similar operations but may stop early based on the length of the list being equal to `n % 10 + 2`. If `n` is between 1001 and 10000, it forces `n` to be 10000 and fills the list accordingly. If `n` is between 10001 and 100000, it forces `n` to be 100000 and behaves similarly. The function then prints the total change (which can vary based on the input) and the length of the list, followed by the elements of the list. The function does not accept any parameters and always produces output based on the generated values.


#State of the program right berfore the function call: **
def func():
    t = int(raw_input())
    ls = []
    while t > 0:
        a = raw_input()
        
        ls.append(a)
        
        t = t - 1
        
    #State of the program after the loop has been executed: `t` is 0, `ls` contains all the values of `a` inputted during the loop iterations, `a` is assigned the value of the last raw input
    dict1 = {}
    for x in ls:
        count = 0
        
        for z in ls:
            if x in z:
                count = count + 1
        
        dict1[x] = count
        
    #State of the program after the  for loop has been executed: `t` is 0, `ls` contains all the values inputted during the loop iterations, `a` is assigned the value of the last raw input, `count` is the total number of times `x` appears in `ls`, `x` is the last value in `ls`, `dict1[x]` is equal to `count`, and `x` is in each `z` in `ls
    sorted_x = sorted(dict1.items(), key=operator.itemgetter(1))
    sorted_x.reverse()
    c2 = 0
    for item in sorted_x:
        if item[1] == 1:
            c2 = c2 + 1
        
    #State of the program after the  for loop has been executed: `sorted_x` contains the items of `dict1` sorted based on the values in descending order, `c2` is the number of items in `sorted_x` where the second element of the item is equal to 1.
    if (c2 > 1) :
        print('NO')
    else :
        print('YES')
        for x in sorted_x:
            c1 = ls.count(x[0])
            
            for z in range(c1):
                print(x[0])
            
        #State of the program after the  for loop has been executed: All characters of all items in `sorted_x` are printed according to their count in `ls`, `sorted_x` has `c1+1` items, count of `x[0]` in `ls` is now `c1+2`, `c1` is assigned the count of `x[0]` in `ls`, `z` is 0
    #State of the program after the if-else block has been executed: *`sorted_x` contains the items of `dict1` sorted based on the values in descending order, `c2` is the number of items in `sorted_x` where the second element of the item is equal to 1. If `c2` is greater than 1, the original state is maintained. Otherwise, all characters of all items in `sorted_x` are printed according to their count in `ls`, `sorted_x` has `c1+1` items, count of `x[0]` in `ls` is now `c1+2`, `c1` is assigned the count of `x[0]` in `ls`, and `z` is 0.
#Overall this is what the function does:The function reads an integer `t` from the user as input. Then, it reads `t` strings and stores them in a list `ls`. After that, it creates a dictionary `dict1` where the keys are the strings from `ls` and the values represent how many times each string appears in `ls`. The function then sorts `dict1` based on the values in descending order and checks if there is more than one item with a count of 1. If there is, it prints 'NO', otherwise it prints 'YES'. Additionally, it prints out the characters based on their count in the sorted dictionary. The function does not accept any parameters and returns the output based on the described conditions.


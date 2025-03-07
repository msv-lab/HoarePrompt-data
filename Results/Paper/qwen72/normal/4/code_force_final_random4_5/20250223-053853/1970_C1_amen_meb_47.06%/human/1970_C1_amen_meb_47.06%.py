def accept_numbers():
    numbers = []
 
    while True:
        nums = input().split()
        if len(nums) != 2:
            break
            
        num1 = int(nums[0])
        num2 = int(nums[1])
 
        numbers.append([num1, num2])
    return numbers
 
result = accept_numbers()
Ron_co=0
Hib_co=0
for sublist in result:
    num_1 = sublist[0]
    num_2 = sublist[1]
    if num_1 > num_2:
        Ron_co+=1
    elif num_1 == num_2:
        continue
    else:
        Hib_co+=1
 
if Ron_co>Hib_co:
    print("Ron")
else:
    print("Hermione")
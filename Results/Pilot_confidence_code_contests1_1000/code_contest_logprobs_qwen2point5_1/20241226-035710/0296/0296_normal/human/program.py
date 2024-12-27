num = input()
list = map(int, raw_input().split())
count1 = 0
count4 = 0
for x in list:
    if x % 2 == 1:
        count1 = count1 + 1
    if x % 4 == 0:
        count4 = count4 + 1
if count1 > count4 and num > 3:
    print("No")
elif num == 2 and count4 - count1 < 0:
    print("No")
elif num == 3 and count4 == 0 and count1 > 0:
    print("No") 
else:
    print("Yes")
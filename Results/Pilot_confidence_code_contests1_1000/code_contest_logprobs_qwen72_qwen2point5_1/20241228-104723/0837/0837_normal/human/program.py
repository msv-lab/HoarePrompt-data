from __future__ import print_function
n = input()
arr = range(1,n+1)
leftnums = []
left = 0
right = 0

if n == 2:
    left = 1
    right = 2
    leftnums = [1]
elif n == 3:
    left = 4
    right = 2
    leftnums = [1, 3]
else :
    for i in range(0,len(arr)/2,2):
        left += arr[i] + arr[len(arr)-i-1]
        leftnums.append(arr[i])
        leftnums.append(arr[len(arr)-i-1])
        right += arr[i+1] + arr[len(arr)-i-2]

if n % 2 == 1 and n != 3:
    right += arr[n/2]

print (abs(left-right))
print (len(leftnums), *leftnums)
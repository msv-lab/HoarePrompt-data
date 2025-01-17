def get_positive_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i and n // i != n:
                divisors.append(n // i)
    return sorted(divisors)

def identical(arr, k):
    # Return True if k is 1

    # Compare the first subarray of length k with other segments
    for i in range(k, n, k):
        if arr[i:i+k] != arr[0:k]:
            return False
            
    return True

    
t = int(input())
test_cases = [(int(input()), input()) for _ in range(t)]
for n, array in test_cases:
    array=[int(i) for i in array.split()]
    p=1
    if (identical(array,1))and n >1:
        p=len(get_positive_divisors(n))+1
        print(p)
        continue
    elif (identical(array,1))and n ==1:
        p=len(get_positive_divisors(n))
        print(p)
        continue
    
    array1=array
    for k in get_positive_divisors(n):
        m=2

        array=array1
        while m<=max(array):
            array=[z%m for z in array]
            if identical(array,k):
                p+=1
                break 
            m+=1
    print(p)  
num_elements=input('Num elements: ')
data=raw_input('Elements: ')
array = data.split(' ')
array = [int(x) for x in array]

def numZeroes(array):
    num=0
    for e in array:
        if e != 0: num+=1
    return num
def resolve():
    if numZeroes(array)<=1:
        print ('NO')
        return
    elif sum(array)!=0:
        print ('YES')
        print ('1')
        print ('1' + ' ' + str(len(array)))
        return
    else:
        i = 0
        while array[i]==0:
            i+=1
        print ('YES')
        print ('1')
        print(str(i+1) + ' ' + str(len(array)))
        return

resolve()

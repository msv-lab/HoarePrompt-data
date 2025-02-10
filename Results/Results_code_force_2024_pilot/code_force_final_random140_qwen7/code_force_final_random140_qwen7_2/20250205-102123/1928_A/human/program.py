for i in range(int(input())):
    a, b = [int(i) for i in input().split()]
    if(a%2==0 and b%2==0):
      print('yes')
    elif(a%2==0 and a/2!=b) or (b%2==0 and b/2!=a):
      print('yes') 
    else:
      print('no')
for i in range(int(input())):
      a = [int(i)for i in input().split()][0]
      p = []
      for i in range(2,a+1,2):p+=[i]
      for i in range(1,a+1,2):p+=[i]
      print(*p)
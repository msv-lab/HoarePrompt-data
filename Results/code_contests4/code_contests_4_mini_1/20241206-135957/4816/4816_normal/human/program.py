import sys

def fun(N, NUMBERS) :
    n = int(N)
    numbers = [int(s) for s in NUMBERS.split(" ")];
    #print str(n)
    #print numbers
    #print n, (len(numbers) + 1)
    assert n + 0 == (len(numbers) + 1)
    sum = 0
    for num in numbers:
      sum += num
    sys.stdout.write(str(int(n * (n+1) / 2 - sum)) + "\n")

if __name__ == "__main__":
   #if False:
   if True:
      n = raw_input()
      numbers = raw_input()
      fun(n, numbers)
   else :
      fun("10", "3 8 10 1 7 9 6 5 2")
   sys.exit(0)
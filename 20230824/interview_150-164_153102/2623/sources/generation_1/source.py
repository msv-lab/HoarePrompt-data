
# function to distribute letters into k strings
def distribute_letters(s, k):

  # sort the letters in s in ascending order
  letters = sorted(list(s))

  # create k empty strings
  strings = [''] * k

  # distribute the letters into the strings
  for i in range(len(letters)):
    strings[i % k] += letters[i]

  # return the minimal possible value of max(a1, a2, ..., ak)
  return min(strings)

# read the number of test cases
t = int(input())

# iterate over the test cases
for _ in range(t):
  # read n (length of string s) and k (number of strings)
  n, k = map(int, input().split())

  # read the string s
  s = input()

  # call the distribute_letters function and print the result
  result = distribute_letters(s, k)
  print(result)

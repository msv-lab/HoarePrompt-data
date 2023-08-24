
# function to distribute letters into k strings
def distribute_letters(s, k):

  # create k empty strings
  strings = [''] * k

  # distribute the letters into the strings
  for i in range(len(s)):
    strings[i % k] += s[i]

  # calculate the maximal possible length among the strings
  max_length = max(len(string) for string in strings)

  # find the first string with maximal length
  max_string = next(string for string in strings if len(string) == max_length)

  # return the minimal possible value of max(a1, a2, ..., ak)
  return max_string

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

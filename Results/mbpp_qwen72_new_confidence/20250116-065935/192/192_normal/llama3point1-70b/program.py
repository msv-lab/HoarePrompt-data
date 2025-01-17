def remove_odd(s):
  return "".join([s[i] for i in range(len(s)) if i % 2 == 0])

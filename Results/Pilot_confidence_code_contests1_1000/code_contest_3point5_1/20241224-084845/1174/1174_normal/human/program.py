s=raw_input()
t=raw_input()

def is_trans_correct(lang1,lang2):
  lang1_rev = ""
  output = "No"
  
  if len(lang1) != len(lang2):
      return output
  
  for i in range(len(lang1)):
    lang1_rev = lang1[i] + lang1_rev
    
  
  if lang1_rev == lang2:
    output = "Yes"
    
  return output
    
    
print(is_trans_correct(s,t))
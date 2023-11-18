def Sorter(text):
   s = len(text)
   for k in range(s):
    wassorted = True
    for i in range(s - k - 1):  
      if int(str(text[i])) > int(str(text[i+1])):
       ii = text
       ii[i], ii[i+1] = ii[i+1], ii[i] 
       wassorted = False 
    if wassorted:
      break  
    return text  
#P.S i don't know if it's already was published/made by other people. I just made this on my free time + i don't claim that this is one and only code like this. But if it is then good!

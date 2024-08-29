
text = input("Enter the string : ")

dict = dict() 
  
words = text.split() 
                         
for word in words: 
    if word in dict: 
        dict[word] = dict[word] + 1
    else: 
        dict[word] = 1
  
for key in list(dict.keys()): 
    print(key, ":", dict[key]) 
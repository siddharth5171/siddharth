# 30/09/2026

# import re

# re.search this methode find the  first match in the text 

# text="i m python learnerr because python is very easy"
# result=re.search("python",text)

# if result:
#     print("found")
# else:
#     print("not found")
# import re
# text=" is easy python "
# print(re.match("python",text))


#   finds all the text at in the line all no of text in line of text 


import re
# text="python is easy python is simple python python  "
# result=re.findall("python",text)
# print(result)

# find the digits in the text 

# text="python is easy 10 20 30  "
# result=re.findall(r"\d+",text)
# print(result)


# find the words in python 
# text="python is easy python is simple python python  "
# result=re.findall(r"\w++",text)
# print(result)

# find the index 
# text="python is easy python is simple python python  "
# result=re.finditer("python",text)
# for match in result:
#     print(match.group(),match.start(),match.end())


#  sub methode is used to replace the word or text 


text="python is easy python is simple python python  "
result=re.sub("python","java",text)
print(result)


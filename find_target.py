# find target string's position  of a given string
given = raw_input('pls string')
target = raw_input('pls target')
# method 1:
# string.find()
position= given.find(target)

# method 1:
# re module 
import re
position2 = re.search(target, given).start()

# method 3:
# slice :
for i in len(given):
   if given[i:i+len(target)]==target:
       position3 = i
# slice may trigger an IndexError: string index out of range
# 


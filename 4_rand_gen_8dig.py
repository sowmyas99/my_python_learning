#1) implement a python program that generates a 8 digit random number and dockerised it

import random
number=0
for num in range(7):
    number=str(number)+str(random.randrange(10))
list=[]
for c in number:
    list.append(c)
print(list)
random.shuffle(list)
print(list)

final_number = ''.join(x for x in list)
print(final_number)

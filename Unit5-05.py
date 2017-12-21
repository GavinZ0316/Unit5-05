# Created by: Gavin Zhou
# Created on: Oct 2017 
# Created for: ICS3U

import random

array = []
number = 0

def getaverage(the_array):
    global number
    count = 0
    for i in array:
        for v in i:
            count = count +1
            number = number + v
    return number/count

print('input rows')

rows = raw_input()

print('input columns')

columns = raw_input()

for i in range(0 , int(rows)):
   array.append([])
   
for i in array:
    for v in range(0, int(columns)):
        i.append(random.randint(1, 50))
    
def getaverage(the_array):
    global number
    count = 0
    for i in array:
        for v in i:
            count = count +1
            number = number + v
    return number/count
    

print(array)
print("average is' ")
print(getaverage(array))

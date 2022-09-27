# Homework_01
# 1.Create list of 100 random numbers from 0 to 1000

import random #import library for useing random function
res_list = [] #create an empty list for edding numbers

for i in range (100): #circle for adding numbers in list
    res_list.append(random.randint (0, 1000)) # use random for chooseing number and append for adding the number in the list
print (res_list, len (res_list)) # print the result

# 2. sort list from min to max (without using sort())
sort_list = True

while sort_list:
    sort_list = False #change sort_list flag for breaking the circle if all values are sorted
    for i in range (len (res_list)-1): # go throught all values in the list
        if res_list [i] > res_list [i + 1]: # compare two values and change their places if it is not sorted
            temp_value = res_list [i] # temp value for changing values
            res_list [i]=res_list [i+1] # change values' places
            res_list [i+1] = temp_value #change values' places
            i = ++1 #increase i
            sort_list = True # change sort_list flag for new circle

print (res_list)
print (sorted (res_list)) # for checking the result

# 3-4. calculate average for even and odd numbers and print the result in console
even_list = [] # empty list for adding even numbers
odd_list = [] # empty list for adding odd numbers

for value in res_list: # circle for adding numbers in even_list and odd_list
    if value % 2 == 0: # compare remainder of the division with 0
        even_list.append(value) # if remainder of the division by 2 is 0, then the number is even and add it in even_list
    else:
        odd_list.append(value) # if remainder of the division by 2 is not 0, then the number is odd and add it in odd_list

# even_list=[] # check empty list
try:
    even_avg = sum (even_list)/len (even_list)
except ZeroDivisionError: 
    print("You tried to divide by zero")
else:
    print('The average result for even list is ', '%.3f' % even_avg)

# odd_list=[] # check empty list
if odd_list==[]: # checking devision by zero with if clause
    print('The list with odd numbers is empty')
else:
    odd_avg = sum (odd_list)/len (odd_list) # sun of values in the odd_list devided by the number of values in the odd_list
    print('The average result for odd list is ', '%.3f' % odd_avg)  # print the average value with 3 numbers after comma


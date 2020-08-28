import math
#Write an equation that uses multiplication, division, an exponent, addition, and subtraction that is equal to 100.25.

#Hint: This is just to test your memory of the basic arithmetic commands, work backwards from 100.25

print((2**2)*25+4-(7.5/2))

# What is the value of the expression 4 * (6 + 5) = 44

# What is the value of the expression 4 * 6 + 5 = 29

# What is the value of the expression 4 + 6 * 5 = 50 --> i know this is incorrect . correct is 34

# What is the type of the result of the expression 3 + 1.5 + 4?
num_calc = 3 + 1.5 + 4
print(type(num_calc)) # type is float. my guess was correct
num1=7
print("Square of a number is %d and Square root of a number is %f"% ((num1**2),(math.sqrt(num1))))

s = 'hello'
# Print out 'e' using indexing
print(s[s.index('e')])


s ='hello'
# Reverse the string using slicing
print(s[::-1])


#Given the string hello, give two methods of producing the letter 'o' using indexing.
s ='hello'
print(s[-1])

print(s[len(s)-1:len(s)])



#Booleans

#What will be the resulting Boolean of the following pieces of code (answer fist then check by typing it in!)

# 2 > 3  False
# 3 <= 2 False
# 3 == 2.0 False
# 3.0 == 3 True 
# 4**0.5 != 2 True -- this is incorrect. it is false

#Checking answers

print(4**0.5 != 2 )  
# 3 <= 2 
# 3 == 2.0 
# 3.0 == 3  
# 4**0.5 != 2 


# two nested lists
l_one = [1,2,[3,4]]
l_two = [1,2,{'k1':4}]

# True or False?
l_one[2][0] >= l_two[2]['k1']
# This should be false


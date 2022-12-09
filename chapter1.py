#                                      chapter 1


'''print function
escape sequence
comments
escape sequence as normal text
python as calculator
variables'''

#print function
print("hello world")
print('hello world')

# strings = collection of characters in single or double quotes

# escape sequence
'''cannot used single quotes in single quotes but we  can used vice versa 
\'  =singlequotes       \t = new TabError
\" = dobles quotes       \\ = single blachslash
\n= new line             \b - back spash '''

print("hello \"world\" world")
print("hello \t world \nBishal")
print("hell\blo")

# comments
# = this is information for user only its not use in program
''' hello'''
# comments= ctrl + forwad slash

# escape sequence as normal text
'''print as it is'''
print("hello \\n line b")
print("this is used for 4 blackslash \\\\\\\\")
#   problem =     output : \" \'
print("\\\" \\\' ")

'''exercise'''
 
#print this line
print("this is\\\\ double blackslash")
print(" these are /\\/\\/\\/\\  mountains")
print(" he is \t awesome")
print (" \\\" \\n \\t \\' ")
print("this is\\blackslash")

# raw string in python
# print as it is.
'''we use r'''
("hello \n line b")
print(r"hello \n line b")

# print emoji 
print("/jgjgsjhg6757")

# calculator
print(2+5*6-8/7)
print(2+4//3*2-2)
'''  / for float
     // for int'''

print(2**2)    #exponent
print(2**0.5)
print(round(2**0.5,4))   #roundoff


'''(),**,*,/,//,%,+,- perceding ordear'''

print(2**3/2*6-4*(3-4/2))  
2**3/2*6-4*3*1
8/12-12

print((2+3)*5/2%6)
5*5/2%6
print(12.5%6)

# exponents
(2**3**2)
print(2**9)

'''  variables'''
# name given to memory location, store any data type, value can be change
num1=2
print(num1)
num1=6
print(num1)

'''Rule: not start from no.
      only start from variables and underdescore
      not use symbol'''

name="bishal"
print(name)

name=123
print(name)

#python snake case writing
first_person_nAME="bishal"
#  java camel case writing 
firstPersonName="ram"
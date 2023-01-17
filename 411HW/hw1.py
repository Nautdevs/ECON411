# Calvin Anderson, Spring 2023 Homework 1
# 1/17/2023

# 1.
x = 'Calvin Anderson'
desc = 'A full-time student at NDSU studying Finance & Accounting. Calvin enjoys a wide variety of subjects such as photography, real estate, philosophy. In his free time he spends it with his significant other and friends.'

# 2.
twoToTheFourth = 2**4 
strpower = str(twoToTheFourth)
sumstrpower = strpower + strpower
sumstrpower

# 3.
escapesequencestr = 'This is my escape sequence string. If you were in a shell, \\ denotes the lines between parent and subdirectories when viewing the output from the \'pwd\' command. \n usually the output is printed on a new line like this.\n You can use \\t in a python string to print a tab character.'
print(escapesequencestr)

# 4.
myfloat = 5.03
myint = 3
myfloat2 = myfloat + myint
type(myfloat2)

# 5.
numerocinco = 2 ** 1024 + 1.1
# The result is an overflow error because this is too large a number to contain in a float object.
numerocinco
# The reason being that a float needs an extra bit to assign the positive negative and needs width for both positive and negative numbers while integers only need width for positive numbers

# 6.
import string
print(string.__dict__)

# 7.
string.digits
string.octdigits
string.printable
string.ascii_letters
string.ascii_uppercase
string.hexdigits
string.punctuation
string.capwords
# Every object in python has an attribute '__dict__' containing that object's dictionary of keys

# 8.
concstring = x + desc + strpower
concstring

from ast import comprehension
import random #random is module for generating random value
import string
#string is a module containing all the string values
 #print(string.ascii_letters)
pass_len = int(input("Enter the desired length for the password: "))
#pass_len = 8
charValues = string.ascii_letters + string.digits + string.punctuation
#list comprehension [function for i in range(n)]
password = "". join([random.choice(charValues) for i in range(pass_len)])
# password = ""
# for i in range(pass_len):
#     password += random.choice(charValues)
print("your random password is :" , password)


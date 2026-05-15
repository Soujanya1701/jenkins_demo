name = "souji:leela::23213:user/tammana"
print(name.split(("/")))

name_1 = "leela soujanya"
print(name_1.split((" ")))

my_name = "tammana"
print(my_name.upper())

my_name_low = "SOUJANYA"
print(my_name_low.lower())

res = my_name+ " "+ name_1
print(res)
print(len(res))

#string built-in functions
str1= "soujanya015"
print(str1[2:5]) #slicing
print(str1[0:5:2]) #slicing with step
print(str1[-1]) #last character
print(str1[::-1]) #reverse string
print(str1.count("a")) #counting occurrences of a character
print(str1.find("j")) #finding index of a character
print(str1.replace("sou", "tam")) #replacing a substring
print(str1.startswith("sou")) #checking if string starts with a substring
print(str1.endswith("ya")) #checking if string ends with a substring
print(str1.isalpha()) #checking if all characters are alphabetic
print(str1.isdigit()) #checking if all characters are digits
print(str1.isalnum()) #checking if all characters are alphanumeric
print(str1.strip("015")) #removing specified characters from the ends of the string
print(str1.strip("sou")) #removing specified characters from the ends of the string

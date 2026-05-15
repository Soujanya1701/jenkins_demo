#creating a list and printing
#also list is mutable so we can add (append) or replace the data
list_1 = [1, 'souji', 20.5, True]
print(list_1)
list_1[1] = "hi"
print(list_1)
list_1.append(16)
print(list_1)

#creating a tuple and printiing 
# tuple is immutable(not changed) so add/remove/append not possible
tuple_1 = ("hello", 20.5, 11)
print(tuple_1)
try:
    tuple_1[1] = "souji"
except TypeError as e:
        print("There is a type error exception", e)
finally:
    print("Final tuple_1:", tuple_1)

#storing tuples inside a list
fruits = [("Apple", 20), ("Orange", 30), ("Mango", 50)]
print(fruits)

#storing list inside tuples
student = ("souji", "soujanya", [20, 9.5])
student[2].append(5)
student[2][0]= "hi"
print(student)

#Task 1: Create an Integer variable for score and a Float for temperature.
score = 50
print(f"score ={score}")
temp = 35.5
print(f"temparture={temp}")

# Task 2: Declare a String variable called book
book = "Amma diary lo konni page lu"
print(f"book name :{book}")
# Task 3: Create a Boolean variable called isdaylight and set it to False.
is_daylight = False
print(is_daylight)
# Task 4: Create a List named mixeddata containing a city name (string)  a temperature (float).
mixed_data = ['pune', 40.5]
print(f"mixed data :{mixed_data}")
# Task 5: Create a Dictionary for a person with keys ”name” and ”hobby”.
dict1 = {'name': "souji", 'hobby': 'sleeping', 'rollno': 20}
print(f"dict:{dict1}")
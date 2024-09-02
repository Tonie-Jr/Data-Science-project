# Understanding between the mutable and immutable objects in python
def get_largest_number(numbers,n):
    numbers.sort()

    return numbers[-n:]

nums = [1, 3, 44, 2, 55, 445, 54, 323, 5433]

print(nums)
largest = get_largest_number(nums, 2)
print(nums)

#Formating the print function using the sep argument
Age = 19
name = "Waihuini"
print("My name is", name, "and I'm ", Age, "years old", sep = "|" )# It is useful when one want to print items with a certain formatting.

#Print items or different statements in the same line. we use the "end = "," " argument to do that
name = "Antony"
print("Hello pycharm", end=", ")
print("I'm", name)

help(name) #The help function is important to give the explanation of whatever in the braces.

#The range function, it is used to iterate values in for loop or to generate a list of numbers.
rng = range(10)
print(rng)
print(list(rng))

#Map function the function allows us to apply the function to every single iterm in an iterable object.
strings = ["My", "World", "Apple", "Pear"]

length1 = map(len, strings)
print(list(length1))

#Example 2 of the map function Using the lambda function

strings = ["My", "World", "Apple", "Pear"]

length2 = map(lambda x: x +"s", strings)
print(list(length2))

#Example 3 of the map function Using my own function
strings = ["My", "World", "Apple", "Pear"]

def add_s(string):
    return string + "s"
length3 = map(add_s, strings)
print(list(length3))

#Filter function
def longer_than_4(string):
    return len(string) > 4

strings = ["My", "World", "Apple", "Pear"]
filtered = filter(longer_than_4, strings)
print(list(filtered))

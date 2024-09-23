# Understanding between the mutable and immutable objects in python


def get_largest_number(numbers,n):
    numbers.sort()

    return numbers[-n:]

nums = [1, 3, 44, 2, 55, 445, 54, 323, 5433]

print(nums)
largest = get_largest_number(nums, 3)
print(largest)
print(nums)

#Formating the print function using the sep argument
Age = 19
name = "Mary"
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

# The sum Function
numbers = {4, 5, 5.43, 5, 6, 6}#set do ho allow duplicate elements. the elements 5 and 6 are removed and then the summation is done.
print(sum(numbers, start= -10))# after the summation, the -10 is added to the total.

#The Sorted Function example 1
print(sorted(numbers))

#The sorted Function example 2 using the key function
people = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 35},
    {"name": "Charlie", "age": 25},
    {"name": "David", "age": 20},
]

Sorted_people = sorted(people, key=lambda person: person["age"], reverse=True)#The reverse function arrange the sorted list a descending order.
print(Sorted_people)

#Enumerate function
tasks = ["cook", "clean", "watch", "code", "Dance"]
for index, task in enumerate(tasks, start = 1):
    print(f"{index}. {task}")

#The Zip function. The zip function is used to combine iterable objects e.g. the list, tuples or the sets
name = ["Antony", "Mary", "John", "Job", "Timothy"]
age = [29, 19, 40, 58]
gender = ["male", "female", "male"]

combined = list(zip(name, age, gender))
print(combined)
for name, age, gender in combined:
    print(f"{name} is {age} years old and is {gender}")

# The open function
#The best practice while working with files is to use of the "with loop" for example below
file = open("test.txt", "w")
file.write("Hello pycharm, \nI'm Antony")
with open("test.txt", "a") as file:
    file.write(" and I love working with data")
with open("test.txt", "r") as file:
    text = file.read()
    print(text)

#example 1 factorial of a number (iteration)
def iterative_factorial(n):
    fact = 1
    for i in range(2, n+1):
        fact *= i
    return fact
print(iterative_factorial(5))
#Example 2 factorial of a number (Recursion)
def recur_factorial(n):
    if n == 1:
        return 1
    else:
        temp = recur_factorial(n-1)
        temp = temp * n
    return temp
print(recur_factorial(6))

#Recursive function that returns all the even numbers less or equal to 8
def EvenNums(num):
    print(num)
    if num % 2 != 0:
        print("Please enter an even number")
    elif num == 2:
        return num
    else:
        return EvenNums(num-2)
print(EvenNums(9))
print(EvenNums(8))

#Fibonacci recursive function
def Fibonacci(indx):
    if indx <= 1:
        return indx
    else:
        return Fibonacci(indx-1) + Fibonacci(indx-2)
print(Fibonacci(8))

#Fibonaccin iterative function
def fibonacci(idx):
    seq = [0,1]
    for i in range(idx):
        seq.append(seq[-1]+seq[-2])
    return seq[-2]
print(fibonacci(88))







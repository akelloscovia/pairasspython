#Lists
#Basic: Create a list of 5 fruits and print each fruit on a new line using a for loop.
#Intermediate: Write a function that takes a list of numbers and returns a new list with each number squared. Example: [1, 2, 3] should become [1, 4, 9].
#Advanced: Write a Python program that takes two lists, list1 = [1, 2, 3] and list2 = [4, 5, 6], and combines them into a single list, combined = [1, 4, 2, 5, 3, 6].
#Challenge: Given a list of numbers, c, write a program to find and print the two largest numbers in the list without using the max() function.


#answer
fruits = ["mango", "apple","orange","guava","strawberry"]
for fruit in fruits: 
 print(fruit)

#intermediate 
def square_numbers(numbers):  # Define a function with a parameter
    square = []  # Initialize an empty list to store squared numbers
    for num in numbers:
        square.append(num ** 2)  # Append the square of each number to the list
    return square  # Return the list after the loop ends
numbers=[1,2,3,4,5]
square= square_numbers(numbers)
print("The squares of the numbers are:", square)

#Advanced
list1=[1, 2, 3]
list2 = [4, 5, 6]
print(list1 + list2)

#Challenge
def get_largest_two(numbers):
    number_sorted = sorted(numbers,reverse=True)#sort the list in descendind order
    return number_sorted[0],number_sorted[1] #return the 1st two elements
numbers=[3,1,4,5,9,2] # Test the function with the given list
largest_two=get_largest_two(numbers)
print("The two largest numbers are:",largest_two)

     



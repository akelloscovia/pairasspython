 #Loops
#Basic: Write a Python program that prints all even numbers between 1 and 20 using a for loop.
#Intermediate: Use a while loop to ask the user to input a number until they provide a number greater than 10.
#Advanced: Write a program that prints the multiplication table (from 1 to 10) for numbers from 1 to 5 using nested for loops.
#Challenge: Given a list of integers, [4, 7, 2, 9, 12, 15], write a program using a for loop to find the sum of all odd numbers and print the result.

#Answer
def even_numbers():
    for even in range(1,21):
        if even % 2==0:
            print(even)
            even_numbers()
    
    #intermediate
    i=0
    while i > 10:
        print(i)
        
        #Advanced
        for i in range(1,6):
            print(f"multiplication table for {i}:")
            for j in range(1,11):
                print(f"{j} x {i}={j*i}")
                print()
                
                #Challenge
                # List of integers
numbers = [4, 7, 2, 9, 12, 15]

# Initialize sum of odd numbers
sum_of_odds = 0

# Iterate through the list
for num in numbers:
    if num % 2 != 0:  # Check if the number is odd
        sum_of_odds += num

# Print the result
print(f"Sum of odd numbers: {sum_of_odds}")
            
            
        
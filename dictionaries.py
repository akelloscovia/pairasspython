#Dictionaries
#Basic: Create a dictionary with three key-value pairs representing a student's information: name, age, and grade. Print each key-value pair on a new line.
#Intermediate:Write a function that takes a dictionary of people's names and their ages, {'Alice': 24, 'Bob': 19, 'Charlie': 30}, and returns a list of names of people who are 21 or older. 
#Advanced: Given a dictionary representing items in a store with their prices, {'apple': 0.5, 'banana': 0.3, 'orange': 0.7}, write a program that takes a list of items bought, ['apple', 'orange', 'banana', 'banana'], and calculates the total cost.
#Challenge: Write a program that counts the occurrences of each word in a given sentence. Example: for the sentence "hello world hello," the output should be {'hello': 2, 'world': 1}.

#Answer
#basic
student={"name":"Scovia",
          "age":"21",
          "grade":"A"
}
name=dict["name"]
print(name)

age=dict["age"]
print(age)

grade=dict["grade"]
print(grade)

    
    #intermediate
the_dict= {"Alice": 24, "Bob": 19, "Charlie": 30}
people_21_or_older = {name: age for name, age in the_dict.items() if age >= 21}
print(people_21_or_older)

#Advanced
dict={'apple': 0.5, 'banana': 0.3, 'orange': 0.7}#list of items and the prices
items_bought={'apple', 'orange', 'banana', 'banana'}# items bought
print(items_bought)
total_cost = sum(dict[item] for item in items_bought)
print(f"Total cost: {total_cost:.2f}")

#challenge
# Input sentence
sentence = "hello world hello"
words = sentence.split()  #Split the sentence into words
# Dictionary to store word counts
word_counts = {}
for word in words:
    word_counts[word] = word_counts.get(word, 0) + 1# Count occurrences of each word
print(word_counts) #print


    
    


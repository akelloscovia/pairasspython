#object-Oriented Programming (OOP)
#Basic: Create a class called Car with attributes brand and color. Instantiate an object of the Car class and print its attributes.
#Intermediate: Add a method called start_engine to the Car class that prints a message saying the engine of the car has started. Create an instance of Car and call the method.
#Advanced: Create a class called BankAccount with attributes account_number and balance. Add methods to:
#Deposit an amount.
#Withdraw an amount (only if sufficient balance exists).
#Print the account balance.
#Challenge: Implement a class called Library that manages a collection of books. Each book has a title, author, and available status. The Library class should have methods to:
#Add a book to the library.
#Remove a book from the library.
#Check if a book is available by title.
#Borrow a book (mark it as unavailable if it’s available).
#Return a book (mark it as available again if it was borrowed).

#Answers
#Basic
class Car:
     def __init__(self, brand, color):
        self.brand = brand
        self.color = color

# Create an instance of the Car class
my_car = Car(brand="subaru", color="black")

# Print the attributes of the object
print(f"Car Brand: {my_car.brand}")
print(f"Car Color: {my_car.color}")

#intermediate
class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def start_engine(self):
        print(f"The engine of the {self.color} {self.brand} has started.")

# Create an instance of the Car class
my_car = Car(brand="subaru", color="black")

# Call the start_engine method
my_car.start_engine()

#Advanced
class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")
    def withdraw(self, amount):
    
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew {amount}. New balance: {self.balance}")
            else:
                print("Insufficient balance for this withdrawal.")
        else:
            print("Withdrawal amount must be positive.")

    def check_balance(self):
        return self.balance

    def display_account_details(self):
        
        print(f"Account Number: {self.account_number}")
        print(f"Balance: {self.balance}")

#challenge
class library:
    def __init__(self ,title,author,available_status): 
      self.title = title
      self.author= author
      self.available_status=available_status
      super().__init__(title,author,available_status)
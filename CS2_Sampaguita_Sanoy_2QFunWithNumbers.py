# Asking for input and initiating variables
age = int(input("Hi there! Please enter your age: "))
sum = 0

# Creating the loop
for i in range(1, age+1):
    sum = sum + i

# Printing of output
print("The sum of all numbers from 1 to", age, "is:", sum)
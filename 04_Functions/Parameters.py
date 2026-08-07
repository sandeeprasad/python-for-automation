def login(username, password):
    print("Opening the application and logging in...")
    print(f"Username: {username}")
    print(f"Password: {password}")
    print("Login successful!")
    print("Closing the application...")
login("Sandeep","Password123")

def add_numbers(num1,num2):
    result=num1+num2
    print(f"The sum of {num1} and {num2} is: {result}")
add_numbers(10,20)
add_numbers(num1=10,num2=20)

""" result = add_numbers(10,20)
print(result*10)  # This will print None because the function does not return a value """


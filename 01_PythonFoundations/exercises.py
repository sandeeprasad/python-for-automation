browser = "chrome"
environment = "QA"
applicationurl = "https://automationexercise.com"
username = "admin@test.com"
password = "Password123"
timeout = 30
retry_count = 3
headless = False

#PRINT ALL THE VALUES

print("==========Automation Configuration==========")
print(f"browser: {browser}")
print(f"environment: {environment}")
print(f"applicationurl: {applicationurl}")
print(f"username: {username}")
print(f"password: {password}")
print(f"timeout: {timeout}")
print(f"retry count: {retry_count}")
print(f"headless: {headless}")

#====================TESTER INFORMATION====================

tester_name = "Sandeep"
experience = 7
primary_skill = "Automation Testing"
city = "Hyderabad"
is_working = True

#====================PRINT ALL THE TESTER INFORMATION========================================

print("\n==========TESTER INFORMATION==========")
print(f"tester_name: {tester_name}")
print(f"experience: {experience}")
print(f"primary skill: {primary_skill}")
print(f"city: {city}")
print(f"is working: {is_working}")

#====================PRINT THE TYPE OF VARIABLES=============================================

print("\n==========TYPE OF VARIABLES==========")
print(type(browser))
print(type(environment))
print(type(applicationurl))
print(type(username))
print(type(password))
print(type(timeout))
print(type(retry_count))
print(type(headless))

#====================PRINT LENGTH OF EACH VARIABLE==========================================

print("\n=========LENGTH VALIDATIONS==========")
print(f"browser length: {len(browser)}")
print(f"environment length: {len(environment)}")
print(f"applicationurl length: {len(applicationurl)}")
print(f"username length: {len(username)}")
print(f"password length: {len(password)}")

#===================USER INPUT==============================================================

print("\n=========USER INPUT==========")
selected_browser = input("Enter browser name: ")
selected_environment = input("Enter the environment: ")

print("\nLAUNCHING AUTOMATION...")
print(f"Browser: {selected_browser}")
print(f"Environment: {selected_environment}")

browser_name = input("Enter name of the browser")
environment_name = input("Enter name of the environment")
headless_test = input("Do you want the test to be headless?").strip().lower()

print(f"browser: {browser_name}")
print(f"environment: {environment_name}")
if headless_test == "true":
    headless_test = True
elif headless_test == "false":
    headless_test = False
else:
    print("Invalid input")








#len()
test_cases = [
    "01_login test",
    "02_validate home page",
    "03_validate dropdowns",
    "04_validate hyperlinks",
    "05_validate images"
]
print(len(test_cases))

#append() - Adds a new element to the list

browsers = [
    "chrome",
    "firefox",
    "edge"
]
browsers.append("safari")
print(browsers)

#insert() - Adds an item at a specific position

variables = [
    "username_field",
    "password_field",
    "login_button",
    "homepage_image"
]

variables.insert(0, "login_url")
print(variables)
variables.insert(2, "login_image")
print(variables)

#remove() - Deletes an item by value

regression_tests = [
    "login_tests",
    "homepage_validation",
    "additem_test",
    "checkout_test",
    "logout_test"
]

print(regression_tests)
regression_tests.remove("additem_test")
print(regression_tests)

#pop() - Deletes the latest added item to the list

failed_tests = [
    "homepage_image",
    "checkout_test",
    "search_test",
    "dropdown_test"
]

print(failed_tests)
print(failed_tests.pop())

#Update values in a list using specific index

homepage_variables = [
    "user_image",
    "user_data",
    "account_summary",
    "hyperlinks"
]

print(homepage_variables)
homepage_variables[2] = "account_details"
print(homepage_variables)

#in operator

supported_browsers = [
    "firefox",
    "chrome",
    "edge",
    "safari"
]
browser = input("Enter your browser name: ").lower()

if browser in supported_browsers:
    print(f"launching {browser} browser..")
else:
    print(f"{browser} browser not supported")




    
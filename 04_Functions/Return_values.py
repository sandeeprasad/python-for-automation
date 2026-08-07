def add_numbers(num1, num2):
    result = num1 + num2
    return result
added_value = add_numbers(10, 20)
print(added_value * 10)  
# This will print 300 because the function returns a value")

def get_page_title():
    return("Schneiders Electric - Global")
title = get_page_title()
if title == "Schneiders Electric - Global":
    print("Title is correct")

def get_browser_name():
    return "Chrome"
browser = get_browser_name()
print(f"Browser name is: {browser}")
if browser == "Chrome":
    print("Browser is Chrome")

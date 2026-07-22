fruits = [
    "apple",
    "orange",
    "banana",
    "blueberry"
]
for fruit in fruits:
    print(fruit)
    
test_results = [
    "PASS",
    "FAIL",
    "PASS"
]
for result in test_results:
    if result == "PASS":
        print("Test case passed!")
    else:
        print("Test case failed!")


for number in range(5):
    print(number)

for device in range(1,6):
    print(f"chekcing device {device}")

test_cases = [
    "login_test",
    "navigate to system management",
    "select the device",
    "validate property panel",
    "generate alarms",
    "logout of user"
]

for index,test in enumerate(test_cases):
    print(index,test)

for index, test in enumerate(test_cases, start=1):
    print(index,test)

topics = [
    "linux",
    "python",
    "git",
    "devops"
]
for index,topic in enumerate(topics,start=1):
    print(index,topic)


numbers = [1,2,3,4,5,6,7]
add_num = 0
for index,num in enumerate(numbers):
    add_num += num
print(add_num)


    



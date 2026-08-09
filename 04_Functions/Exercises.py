def connect_server(environment="QA"):
    print(f"Connecting to the {environment} server...")
connect_server()
connect_server("Production")
connect_server("Staging")

def create_user(username,age,city):
    print(f"username: {username}"),
    print(f"age: {age}")
    print(f"city: {city}")

create_user("Sandeep", 33, "Hyderabad")
create_user(username="swathi", city="Bangalore", age=30)

def login(username,password,environment="QA"):
    print("Connecting to QA server...")
    print(f"Logging in with username: {username} and password: {password}")
    print(f"Executing login in {environment}")

login(password="user123",username="sandeep")

tests = ["login_test",
         "payment_test",
         "checkout_test",
         "logout_test"]

def execute_tests(tests, browser="Chrome"):
    print("===================================")
    for test in tests:
        print(f"Executing {test}...")
        print(f"browser used is: {browser}")
        print(f"status : {test}_passed")
    print("===================================")

execute_tests(browser="firefox", tests=tests)

tests_cases = [
    "login",
    "payment",
    "checkout",
    "logout"
]

def run_test(test_name):
    print(f"Running {test_name} test...")
    if test_name == "payment":
        return "FAIL", 3.8
    else:
        return "PASS", 2.4

Passed = 0
Failed = 0
for test in tests_cases:
    status, execution_time = run_test(test)
    print(f"Test status: {status}")
    print(f"execution time: {execution_time}")
    if status == "PASS":
        Passed +=1
    elif status == "FAIL":
        Failed +=1
print(f"Total Passed: {Passed}")
print(f"Total Failed: {Failed}")    



    

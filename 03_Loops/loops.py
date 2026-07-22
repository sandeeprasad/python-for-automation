#Example 1

test_cases = [
    "Login Test",
    "Search Test",
    "Checkout Test",
    "Logout Test"
]
for test_case in test_cases:
    print(f"Executing: {test_case}")

#Example 2

browsers = [
    "Chrome",
    "Firefox",
    "Edge"
]
for browser in browsers:
    print(f"Running tests on: {browser}")

#Example 3 

api_endpoints = [
    "/login",
    "/users",
    "/products",
    "/orders"
]
for api in api_endpoints:
    print(f"Testing API: {api}")

#Example 4 - Multiple Environments

environments = [
    "QA",
    "UAT",
    "Production"
]
for environment in environments:
    print(f"Deploying tests to: {environment}")
    
#COMBINING THE FOR LOOP AND IF CONDITION

passed = 0
failed = 0

test_execution = [
    ("TC_01 : Login", "PASS"),
    ("TC_02 : Navigate to system management page", "PASS"),
    ("TC_03 : Select a device on the canvas", "PASS"),
    ("TC_04 : Validate that the property panel exists", "FAIL")
]

for test, result in test_execution:
    print(f"\nEXECUTING {test}")
    if result == "PASS":
        print(f"Result : {result}")
        passed +=1
    else:
        print(f"Result : {result}")
        failed +=1

print("\n==========EXECUTION SUMMARY==========")
print(f"Passed: {passed}")
print(f"Failed: {failed}")



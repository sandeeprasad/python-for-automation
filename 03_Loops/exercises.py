smoke_suite = [
    "Login Test",
    "Logout Test",
    "Forgot Password Test"
]
for test in smoke_suite:
    print(f"executing: {test}")

supported_browsers = [
    "Chrome",
    "Firefox",
    "Edge"
]
for browser in supported_browsers:
    print(f"Launching {browser}")

api_endpoints = [
    "/login",
    "/products",
    "/users",
    "/cart"
]
for api in api_endpoints:
    print(f"Testing {api}")

failed_tests = [
    "Search Test",
    "Payment Test",
    "Profile Test"
]
for failed_test in failed_tests:
    print(f"Re-running: {failed_test}")

regression_tests = [
    "TC_01 : Login to portal as automation engineer",
    "TC_02 : Login to portal as maintenance engineer",
    "TC_03 : Login to portal as security engineer",
    "TC_04 : Select the solution and navigate to system management page"
]
print("==========Regression Suite Execution==========")
for tests in regression_tests:
    print(f"Executing {tests}...")
print("Regression execution completed.")

Passed = 0
Failed = 0
device_status = [
    ("TC_01 : check asrock health status", "PASS"),
    ("TC_02 : check AP310 health status", "PASS"),
    ("TC_03 : check ATVd health status", "FAIL"), 
    ("TC_04 : check M580D health status", "FAIL"),
    ("TC_05 : check softdpac running status", "PASS")
]

print("\nExecuting tests...")
for test,status in device_status:
    
    if status == "PASS":
        print(f"{test} : {status}")
        Passed +=1
    else:
        print(f"{test} : {status}")
        Failed +=1
print("Device status checked..")

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

for index, test in enumerate(test_cases, start=1):
    print(f"executing test {index}: {test}")

for attempt in range(1,4):
    print(f"Retry attempt {attempt}")

for device in range(1,6):
    print(f"Checking Device: {device}")

for index,test in enumerate(test_cases,start=1):
    print(f"Executing test case {index}")
    print(f"TC_0{index} : {test}")

execution_status = [
    "PASS",
    "FAIL",
    "PASS",
    "PASS",
    "FAIL",
    "PASS",
    "PASS"
]
Passed=0
Failed=0
print("==========Regression Execution==========")
for index,result in enumerate(execution_status, start=1):
    print(f"executing test: {index}")
    print(f"result: {result}")
    if result=="PASS":
        Passed+=1
    else:
        Failed+=1
print("========================================")
Total_Tests=Passed+Failed
print(f"total tests: {Total_Tests}")
print(f"passed tests: {Passed}")
print(f"failed tests: {Failed}")

devices = [
    "asrock",
    "m580d",
    "crd",
    "atvd",
    "softdpac"
]
for index,device in enumerate(devices, start=1):
    print(f"\nExecuting test case {index}")
    print(f"Device name: {device}")

for attempt in range(1,4):
    print(f"Retry attempt: {attempt}")

print("maximum retry limit reached.")

browsers =[
    "chrome",
    "edge",
    "firefox"
]
for number,browser in enumerate(browsers,start=1):
    print(f"\nlaunching browser {number}")
    if browser=="chrome":
        for test1 in range(1,3):
            print(f"\nexecuting smoke test {test1}")
    elif browser=="edge":
        for test2 in range(1,3):
            print(f"\nexecuting smoke test {test2}")
    elif browser=="firefox":
        for test3 in range(1,3):
            print(f"\nexecuting smoke test {test3}")
    else:
        print("broser not found")

##-----Above code could have been written as-------------##

browsers = [
    "chrome",
    "edge",
    "firefox"
]

for number, browser in enumerate(browsers, start=1):

    print(f"\nLaunching Browser {number}: {browser}")

    for smoke_test in range(1, 3):
        print(f"Executing Smoke Test {smoke_test}")
    


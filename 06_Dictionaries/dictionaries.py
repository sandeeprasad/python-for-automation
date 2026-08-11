#Update existing key value in dictionary

test_case={
    "name": "Login Test",
    "browser": "Chrome",
    "priority": "High",
    "status": "Not executed"
}
print("Before Execution")
print(test_case)
test_case["status"]="Pass"
print("After Execution")
print(test_case)

test_case["execution_time"]="5 seconds"
print(test_case)

test_case={
    "name": "Logout Test",
    "browser": "Firefox",
    "priority": "Medium",
    "status": "Not executed"
}

print(test_case)
test_case["status"]="Pass"
print(test_case)
test_case["execution_time"]="3 seconds"
print(test_case)
test_case["environment"]="QA"
print(test_case)
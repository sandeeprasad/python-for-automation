test_cases={
    "name": "Login Test",
    "browser": "Chrome",
    "priority": "High",
    "status": "Not executed"
}

print(test_cases["name"])
print(test_cases["browser"])
print(test_cases["priority"])
print(test_cases["status"])

test_case = {
    "id": "TC_001",
    "name": "Login Test",
    "browser": "Chrome",
    "environment": "QA",
    "priority": "High",
    "status": "Not Executed",
    "execution_time": 0,
    "retry_count": 0
}
test_case["status"] = "Pass"
test_case["execution_time"]=4
test_case["browser"]="Firefox"
test_case["environment"]="Staging"
test_case["owner"]="Sandeep"
test_case.pop("retry_count")
print(test_case.keys())
print(test_case.values())
print(test_case.items())
print(test_case.get("owner"))
print(test_case.get("screenshot"))
print(test_case)

test_case = {
    "id": "TC_001",
    "name": "Login Test",
    "browser": "Firefox",
    "environment": "Staging",
    "priority": "High",
    "status": "PASS",
    "execution_time": 4,
    "owner": "Sandeep"
}

for test in test_case.keys():
    print(test)
for test in test_case.values():
    print(test)

print("="*30)
print("TEST CASE DETAILS")
print("="*30)
for key,value in test_case.items():
    print(f"{key}: {value}")

test_case = {
    "id": "TC_007",
    "name": "Payment Test",
    "browser": "Chrome",
    "environment": "QA",
    "priority": "Critical",
    "status": "Not Executed",
    "execution_time": 0,
    "retry_count": 0
}
print("="*30)
print("BEFORE MODIFICATIONS")
print("="*30)
for key, value in test_case.items():
    print(f"{key} : {value}")


test_case["browser"] = "Firefox"

test_case["environment"] = "Staging"

test_case["status"] = "PASS"

test_case["execution_time"] = 5

test_case["owner"] = "Sandeep"

test_case["build"] = "Build_105"

test_case["defect_id"] = "BUG_3421"

test_case.pop("retry_count")
print("="*30)
print("AFTER MODIFICATIONS")
print("="*30)
for key, value in test_case.items():
    print(f"{key} : {value}")
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
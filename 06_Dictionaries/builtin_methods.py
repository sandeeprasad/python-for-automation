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

print(test_case.keys())
print(test_case.values())
print(test_case.items())
print(test_case.get("name"))
print(test_case.get("owner", "Unknown"))
print(test_case.pop("retry_count"))
print(test_case)



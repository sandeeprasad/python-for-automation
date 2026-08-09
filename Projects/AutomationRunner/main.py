import browser
import login
import report
import runner

test_cases= [
    "Login Test",
    "Payment Test",
    "Checkout Test",
    "Logout Test"
]
passed = 0
failed = 0
for test in test_cases:
    browser.launch_browser()
    login.login("admin","admin123")
    status = runner.execute_test(test)
    browser.close_broswer()
    if status == "PASS":
        passed +=1
    else:
        failed +=1
report.generate_report(passed,failed)
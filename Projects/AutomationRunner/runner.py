def execute_test(test):
    
    if test == "Payment Test":
        print("Payment Test Failed!")
        return "FAIL"
    else:
        print(f"{test} Passed!")
        return "PASS"
def login(username,password):
    print(f"Logging in with username: {username}")
    if username == "admin" and password == "admin123":
        print("Login Successful!")
        return "Success!"
    return "Login Failed!"
    
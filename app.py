
# Predefined credentials
USERNAME = "admin"
PASSWORD = "password"

def login():
    print("Welcome to the Login System")
    entered_username = input("Enter your username: ")
    entered_password = input("Enter your password: ")
    
    if entered_username == USERNAME and entered_password == PASSWORD:
        print("Login Success! Welcome!")
    else:
        print("Login Failed! Invalid username or password")

if __name__ == "__main__":
    login()

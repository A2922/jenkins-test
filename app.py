
# Predefined credentials
USERNAME = "admin"
PASSWORD = "password"

def login():
    # Use predefined credentials directly
    entered_username = "admin"
    entered_password = "password"
    
    print("Welcome to the Login System")
    print(f"Username: {entered_username}")
    print(f"Password: {entered_password}")
    
    if entered_username == USERNAME and entered_password == PASSWORD:
        print("Login Success! Welcome!")
    else:
        print("Login Failed! Invalid username or password")

if __name__ == "__main__":
    login()

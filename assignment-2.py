'''
Assignment 2 - Deadline (Saturday, August 17, 8:00 PM)

QUESTION WAP that first gives 2 options:

Sign up
Sign in
when 1 is pressed user needs to provide following information

Username, 2. Password, 3. Mobile number All this information is saved in a file everytime a new user signs up the same 
file is updated (hint Append over the same file)
when 2 is pressed User needs to provide username and password this username and password is checked with username 
and password in the database if matched: welcome to the device and show their phone number else: terminate the program 
saying incorrect credentials

Do it using json files, save everything to json and load from json
'''
import json

def sign_up(filename):
    n=1
    username=input("Enter username")
    password=input("Enter password")
    rpassword=input("Enter rpassword")
    
    while(password != rpassword and n!=3):
        print("password mismatch")
        password=input("Enter password")
        rpassword=input("Enter confirm password")
        n+=1
    if n >= 3 and password != rpassword:
        print("Too many wrong attempts. Signup failed.")
    else:
        mobile = input("Enter mobile number: ")
        new_user = {
            username: {
                'password': password,
                'mobile': mobile
            }
        }
        
        try:
            try:
                with open(filename, 'r') as f:
                    data = json.load(f)
            except (FileNotFoundError, json.JSONDecodeError):
                data = {}
            data.update(new_user)
            with open(filename, 'w') as f:
                json.dump(data, f, indent=4)

            print("Signup successful!")
        except Exception as e:
            print(f"An error occurred: {e}")

    
def sign_in(filename):
    print("Username: ")
    username=input("Enter username")
    password=input("Enter password")
    try:     
        with open(filename) as f:
            data=json.load(f)
            print(data)
    except Exception as e:
        print(e)
    if username in data and data[username]['password']==password:
        print(f"Username: {username}")
        print(f"Mobile no.: {data[username]['mobile']}")
    else:
        print(f"{username} does not exist in database")
        
def main():
    filename="info.json"
    print("1. Sign In\n2. Sign Up\n3. Exit")
    option=int(input("Enter option"))
    
    if option==1:
        sign_in(filename)
    elif option==2:
        sign_up(filename)
    elif option==3:
        print("Exiting...")
    else:
        print("Invalid option please try again")
        main()
        
    
if __name__ == "__main__":
    main()



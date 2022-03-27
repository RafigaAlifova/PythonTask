password = "admin123"
username = "admin"
loginun = input("Enter username: ")
count = 0
if loginun == username:
    while count < 3:
        loginpw = input("Enter password: ")
        if loginpw != password:
            count += 1
            if count == 3:
                print("System blocked for 15 minutes")
            else:
                print("Try again")
        else:
            print("Successfully logined!")
            break
else:
    print("Incorrect username")
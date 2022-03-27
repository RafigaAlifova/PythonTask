lengthCount= True
while lengthCount:
    password = input(" enter password: ")
    if (8 <= len(password) <= 13):
        print("Correct!")
        lengthCount=False
        break
    else:
        print("password must be between 8 and 13 characters")
       
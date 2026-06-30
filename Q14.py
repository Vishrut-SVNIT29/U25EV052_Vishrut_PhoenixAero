#Q14 User ID and password validation

#predefined credentials
correct_user = "phoenix10"
correct_password = "drone123"

#user input
user = input("Enter User ID: ").lower()
password = input("Enter Password: ").lower()

#compare credentials
if user == correct_user and password == correct_password:
    print("Drone connected successfully!")
else:
    print("Invalid User ID or Password.")
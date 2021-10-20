passwords = ["Ceramic20Cube!"]
names = ["Ceramic cube"]
name = input("Enter name: ")
password = input("Enter password: ")

if password == passwords[0] and name == "Ceramic cube":
    print(f"Hi! {name}")
else:
    print("You did not get into the admin panel!")
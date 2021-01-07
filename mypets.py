# The "in" and "not" operators

my_pets = ["Greg", "Emma", "Pepita", "Carmelo"]
print("Enter the name of one of your pets: ")

while True:
    name = input()
    if name not in my_pets:
        print("I'd love to have a pet named " + name)
    else:
        print(name + " is my pet!")
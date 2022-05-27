name = input("Please enter your name: ")
print(f"\nHello, {name}!")

name2 = input("Please input your other name, not {name}: ")
print(f"\nHello, {name2}, you are not {name}.")

prompt = "If you tell use who you are, we can personalize " \
    "the messages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print(f"\nHello, {name}!")
import random

def generate_password(lengths):
    passwords = []
    for length in lengths:
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        password = ''.join(random.choice(alphabet) for _ in range(length))
        password = replace_with_number(password)
        password = replace_with_uppercase_letter(password)
        passwords.append(password)
    return passwords

def replace_with_number(password):
    for _ in range(random.randrange(1, 3)):
        replace_index = random.randrange(len(password)//2)
        password = password[:replace_index] + str(random.randrange(10)) + password[replace_index+1:]
    return password

def replace_with_uppercase_letter(password):
    for _ in range(random.randrange(1, 3)):
        replace_index = random.randrange(len(password)//2, len(password))
        password = password[:replace_index] + password[replace_index].upper() + password[replace_index+1:]
    return password

def main():
    num_passwords = int(input("How many passwords do you want to generate? "))
    print("Generating {} passwords".format(num_passwords))

    password_lengths = []

    print("Minimum length of password should be 3")

    for i in range(num_passwords):
        length = int(input("Enter the length of Password #{}: ".format(i+1)))
        if length < 3:
            length = 3
        password_lengths.append(length)

    passwords = generate_password(password_lengths)

    for i, password in enumerate(passwords):
        print("Password #{} = {}".format(i+1, password))

main()

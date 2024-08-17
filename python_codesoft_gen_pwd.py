import random
import string

def gen_pwd(length):

    uprcase_letters = string.ascii_uppercase
    lwrcase_letters = string.ascii_lowercase
    digits = string.digits
    special_characters = string.punctuation
    all_characters = uprcase_letters + lwrcase_letters + digits + special_characters
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

def main():
    
    while True:
        try:
            length = int(input("Enter the length of the password: "))
            if length<12:
                print("Password length should be at least 12 characters maintained.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter the correct characters.")
    
    
    password = gen_pwd(length)
    print(f"Generated password: {password}")

if __name__ == "__main__":
    main()

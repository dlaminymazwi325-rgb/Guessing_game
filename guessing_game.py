import random
name= input("Enter your name: ").title()
surname= input("Enter your surname: ").title()
gender= input("Enter your gender. (Mr/Mrs): ").title()
age= int(input("Enter your age: "))
full_name=name+" "+surname
print()

if age >= 18:
    print("you are eligable to play")
    print(f"hello {gender} {full_name}. Welcome to Mazwi`s guessing game. The instructions are as follows:")
    print("1. Guess the number between 0 and 10.\n"
          "2. You only have 3 attempts.\n"
          "3. Once attempts are finished, you will be out of the game.\n"
          "4. Correct guess will win you a prize of E5000.\n")
    print()

    next_step=input("Do you want to continue? (y/n): ").lower()
    if next_step=="y" or next_step=="yes":
        number = random.randint(0, 10)
        attempts = 3
        print("Guess the number between 0 and 10. You have", attempts, "attempts")
        
        while attempts > 0:
            try:
                guess = int(input("Enter your guess: "))
            except ValueError:
                print("Please enter a valid number.")
                continue

            attempts = attempts - 1
            if guess == number:
                print()
                print("congrats, you guessed right. You have just won yourself a prize of E5000. please give us your contact details so we contact you when your prize is ready.")
                print("Choose which way you want us to contact you\n"
                      "1. Phone call\n"
                      "2. Whatsapp\n"
                      "3. Email")
                print()
                choice=input("Enter your choice: ")
                if choice=="1":
                    phone_number=input("Enter your phone number: ")
                    print()
                    print(f"Thank you {gender} {full_name} for playing. We will contact you soon for your prize collection.\n"
                           "Processing will take at least 2 working days ")

                elif choice=="2":
                    whatsapp_number=input("Enter your whatsapp number: ")
                    print()
                    print(f"Thank you {gender} {full_name} for playing. We will contact you soon via whatsapp for your prize collection.\n"
                           "Processing will take at least 2 working days ")
                elif choice=="3":
                    email=input("Enter your email: ").lower()
                    print()
                    if "." not in email or "@" not in email:
                        while True:
                            print("Invalid email. Please enter a valid email address")
                            email = input("Enter your email: ").lower()
                            if "." in email and "@" in email:
                                break
                    print()

                    print(f"Thank you {gender} {full_name} for playing. We will contact you soon via email for your prize collection.\n"
                               "Processing will take at least 2 working days ")
                else:
                    print("Invalid choice. Please enter a valid choice")

                break

            elif guess != number and attempts != 0:
                print("You guessed wrong!..... try again,", attempts, "attempts left")
                continue
            elif guess != number and attempts == 0:
                print("You guessed wrong! You are out of the game.")
    else:
        print()
        print("Thank you. Goodbye")
else:
    print()
    print("Age below 18. You are not eligable to play")
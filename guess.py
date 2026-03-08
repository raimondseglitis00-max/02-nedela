import random

while True:  # spēles cikls (lai varētu spēlēt vēlreiz)
    number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10

    print("\nUzmini skaitli no 1 līdz 100!")

    while True:
        guess = input("Tavs minējums: ")

        try:
            guess = int(guess)
        except ValueError:
            print("Lūdzu ievadi skaitli!")
            continue  # turpina spēli

        attempts += 1

        if guess < number:
            print("Par mazu")
        elif guess > number:
            print("Par lielu")
        else:
            print(f"Pareizi! Uzminēji {attempts} mēģinājumos.")
            break

        if attempts >= max_attempts:
            print(f"Beidzās mēģinājumi! Pareizais skaitlis bija {number}.")
            break

    # piedāvā spēlēt vēlreiz
    again = input("Spēlēt vēlreiz? (j/n): ")
    if again.lower() != "j":
        print("Paldies par spēli!")
        break
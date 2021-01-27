import random
import string
import pyperclip


def pass_gen():
    needs_upper = False
    needs_numbers = False
    needs_symbols = False

    characters = string.ascii_letters + string.digits + string.punctuation
    raw_password = []
    while True:
        size = int(input('SIZE OF PASSWORD: '))
        if size < 6:
            print('MUST BE 6 OR MORE CHARACTERS!')
            continue
        if size > 24:
            print('CANNOT BE LONGER THAN 24 CHARACTERS!')
            continue
        break

    choice = input('NEED CAPITAL LETTERS (Y/N)?: ').lower()
    if choice == 'y':
        needs_upper = True
    else:
        needs_upper = False
    choice = input('NEED NUMBERS (Y/N)?: ').lower()
    if choice == 'y':
        needs_numbers = True
    else:
        needs_numbers = False
    choice = input('NEED SYMBOLS (Y/N)?: ').lower()
    if choice == 'y':
        needs_symbols = True
    else:
        needs_symbols = False

    requirements = (needs_upper, needs_numbers, needs_symbols)
    print(requirements)
    # ------------------------------------------------------ #
    passes = 0
    while True:
        for i in range(size):
            raw_password.append(random.choice(characters))
        # ------------------------------------------------------ #
        for character in raw_password:

            print(character)
            if needs_upper:
                if character in string.ascii_uppercase:
                    needs_upper = False
            print(needs_upper)
            # ------------------------------------------------------ #
            if needs_numbers:
                if character in string.digits:
                    needs_numbers = False
            print(needs_numbers)
            # ------------------------------------------------------ #
            if needs_symbols:
                if character in string.punctuation:
                    needs_symbols = False
            print(needs_symbols)
        # ------------------------------------------------------ #
        if any((needs_upper, needs_numbers, needs_symbols)):
            print(f'Requirements not met, making new password.')
            passes += 1
            print(f'PASSES: {passes}')
            raw_password.clear()
            print(requirements)
            needs_upper, needs_numbers, needs_symbols = requirements
            print(needs_upper, needs_numbers, needs_symbols)
            continue
        break
        # ------------------------------------------------------ #
    formatted_password = ''.join(raw_password)
    print(f'\nNEW PASSWORD: {formatted_password}')
    print('NEW PASSWORD IS COPIED TO CLIPBOARD')
    passes += 1
    print(f'PASSES: {passes}')
    pyperclip.copy(formatted_password)


pass_gen()
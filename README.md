# passgen
CLI password generator that allows for alphanumeric conditions

Run the passgen.py file from an editor or the command line.

Prompts user for a password size. Must be between 6 adn 24 characters.

Asks user if the password needs to contain at least one of the following:
- uppercase letters
- numbers
- symbols/punctuation

Returns a password that meets the requirements and automatically copies the result to the clipboard.
- The automatic copy to clipboard only works in windows through pyperclip


For fun, the terminal will show every character sequence the program tried to make and
whether or not it met the conditions the user specified in the beginning. The program
will log how many passes or tries it took to create an acceptable password.

  - the options picked for the password will be displayed as booleans in the order: (uppercase, numbers, symbols)
  - for example if the user did not need uppercase characters but did need at least one number and one symbol,
  - this would display as (False, True, True)
  - the character picked will be displayed
  - if the character satisfied a password requirement, the corresponding boolean value will be switch to False.
  - this is to designate that the password no longer needs a character of that type because it now has at least one.
  - if at the end of randomly selecting characters equal to the number specified, the password does not return
  - (False, False, False) mean that the password no longer needs one of the corresponding character types,
  - the password will pass and be copied to the clipboard.
  - if not, the generator will try again, and continue to do so untill a generation satisfies the beginning conditions
  
  

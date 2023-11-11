"""
Random password generator
Author: Malcolm White
Date: 2023-11-10
This random password is a console-based program that provides a unique,
dynamic password with as many characters as the user would like.
"""

import os
import random as random
from slowtype import slowtype
from time import sleep


password_length = 0
interface_active = True
valid_choices = ('y','n')
special_data = ['!','@','#','$','_','-','+']
element_data = ['a','b','c','d','e','f','g','h','i','j','k','l','m','o','p',
                'q','r','s','t','u','v','w','x','y','z','A','B','C','D','E',
                'F','G''H','I','J','K','L','M','N','O','P','Q','R','S','T',
                'U','V','W','X','Y','Z','1','2','3','4','5','6','7','8','9']


# Interface

while interface_active:

    slowtype('PASSWORD GENERATOR\n', 0.02)
    sleep(0.5)
    slowtype('BY MALCOLM WHITE\n', 0.02)
    sleep(0.5)
    keep_going = True

    while keep_going:

        # Getting password length
        decision = input('Please enter the desired password length: ')
        password_length = decision
        valid = decision.isnumeric()

        try:

            if valid != True:
                raise ValueError
            elif int(decision) == 0:
                raise ValueError
            else:
                password_length = int(password_length)
                password = ''
            
            # Asking for special characters
            while True:  
                special = input('Would you like to include special characters? Y/N: ')
                special = special.lower()
                valid_choices = ('y','n')

                if special not in valid_choices:
                    print('Please choose either Y/N.')
                    continue

                elif special == 'y':
                    element_data += special_data

                # Generating password
                for i in range(0, password_length):
                    random_char = random.choice(element_data)
                    password += random_char

                slowtype(f'Here is your randomly generated password: {password} \n',0.02)
                break

            #Asking if user would like another password
            while True:
                try_again = input('Would you like to generate another password? Y/N: ')
                try_again = try_again.lower()

                if try_again == 'y':
                    break

                # Exit
                elif try_again == 'n':
                    slowtype('Thank you for using my program!', 0.02)
                    sleep(1.5)
                    interface_active = False
                    os.system('cls')
                    keep_going = False
                    break
                else:
                    print('Please select either Y/N.')

        except ValueError:
            print('Password length must be a whole, positive number.')
            
os.system('cls')
        
            

        



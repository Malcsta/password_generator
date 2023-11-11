# Setup

import os
import random as random
from slowtype import slowtype
from time import sleep



password_length = 0
interface_active = True
element_data = ['a','b','c','d','e','f','g','h','i','j','k','l','m','o','p',
                'q','r','s','t','u','v','w','x','y','z','A','B','C','D','E',
                'F','G''H','I','J','K','L','M','N','O','P','Q','R','S','T',
                'U','V','W','X','Y','Z','1','2','3','4','5','6','7','8','9',
                '!','@','#','$']
valid_choices = ('y','n')

# Interface

while interface_active:

    slowtype('PASSWORD GENERATOR\n', 0.02)
    sleep(0.5)
    slowtype('BY MALCOLM WHITE\n', 0.02)
    sleep(0.5)
    keep_going = True

    while keep_going:
        decision = input('Please enter the desired password length: ')
        password_length = decision
        valid = decision.isnumeric()

        try:
            if valid != True:
                raise ValueError
            else:
                password_length = int(password_length)
                password = ''
                for i in range(0, password_length):
                    random_char = random.choice(element_data)
                    password += random_char
                    
            slowtype(f'Here is your randomly generated password: {password} \n',0.02)
            try_again = input('Would you like to generate another password? Y/N: ')
            try_again = try_again.lower()
            if try_again == 'y':
                continue
            elif try_again == 'n':
                os.system('cls')
                keep_going = False
        except ValueError:
            print('Please enter a whole number.')
            
        
        
            

        



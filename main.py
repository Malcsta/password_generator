

# Setup

import os
import random as random
from slowtype import slowtype
from time import sleep



valid_decisions = ('y', 'n')
password_length = 12
interface_active = True
element_data = ['a','b','c','d','e','f','g','h','i','j','k','l','m','o','p',
                'q','r','s','t','u','v','w','x','y','z']


# Interface

while interface_active:
    slowtype('PASSWORD GENERATOR\n', 0.05)
    sleep(0.5)
    slowtype('BY MALCOLM WHITE\n', 0.05)
    sleep(0.5)
    decision = input('Would you like to generate a password? Y/N: ')
    decision.lower()

    if decision not in valid_decisions:
        print('Invalid Selection.')
    
    elif decision == 'y':
        letter_one = random.choice(element_data)
        letter_one.upper()
        letter_two = random.choice(element_data)
        letter_three = random.choice(element_data)
        letter_four = random.choice(element_data)
        letter_four.upper()
        letter_five = random.choice(element_data)
        letter_six = random.choice(element_data)
        letter_six.upper()
        letter_seven = random.choice(element_data)
        letter_eight = random.choice(element_data)
        letter_nine = random.choice(element_data)
        letter_ten = random.choice(element_data)
        letter_eleven = random.choice(element_data)
        letter_twelve = random.choice(element_data)
        
        passnum = random.randint(1000,9999)
        str(passnum)

        password = (letter_one +
                    letter_two +
                    letter_three +
                    letter_four +
                    letter_five +
                    letter_six +
                    letter_seven +
                    letter_eight +
                    letter_nine +
                    letter_ten +
                    letter_eleven +
                    letter_twelve)
                    
        
        print(password)
        


     

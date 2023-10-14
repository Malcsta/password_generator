"""
Description: Slowtype function
Author: Malcolm White
Date: 2023-10-05
Usage: This modular function can be used to write messages to the console in
timed sequence, letter by letter. The function takes two parameters: the 
message (string), as well as the speed (int or float) at which you'd like the
message to be displayed. 
"""

import time 
from time import sleep
import sys
import os

def slowtype(message, texttime):
    string_to_type = message
    for char in string_to_type:
        sys.stdout.write(char)
        sys.stdout.flush()
        text_time = texttime
        time.sleep(text_time)




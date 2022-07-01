from user_functions import make_exit, match_intent
from responses import ask_why_response, automated_responses, exit_msg
import re

import sys



def chat():
    reply = input("How can the Mechanically Intilectualized Neurological Dataset Computerized Retro Automic Fortune Teller, or MIND CRAFT for short, impress you today?\n").lower()
    if make_exit(reply) == True:
        sys.exit(exit_msg)
    while not make_exit(reply):
            reply = input(match_intent(reply))




    
chat()

#testing match_reply function
#return match_reply("what is the aries sign?")
#print(match_reply("what is the virgo sign"))

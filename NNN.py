# ============================================================================
# <Delete any lines or entries you don't want or need... like this line>
# Source: <your name, company, or organization  - <your web site like www.steamclown.org> 
# GitHub: <if you don't have a github link, then delete this line>
# Hacker: <your name - NickName, <more nouns to describe how awesome you are Engineer, Maker, > 
# This example code is licensed under the CC BY-NC-SA 4.0, GNU GPL and EUPL
# https://creativecommons.org/licenses/by-nc-sa/4.0/
# https://www.gnu.org/licenses/gpl-3.0.en.html
# https://eupl.eu/
# Program/Design Name:		<nameYourProgram.py>
# Description:    This is a template for python programs... change this for your 
# program description... should be 1-4 lines
# Dependencies:   python3
#   Python Libraries Used:  
#      <List any Libraries>   
#   Inputs: <list any expected user input here>
#   Outputs: <list any expected program output here>
# Revision: 
#  Revision 0.03 - Updated 06/09/2025 <add your update description here>
#  Revision 0.02 - Updated 01/09/2025 added 'input / output' to the Dependencies section 
#  Revision 0.01 - Created 01/07/2025
# Additional Comments: 
# 
# ============================================================================

def main():
    number = get_number()
    meow(3)


def get_number():
    while True: 
        n = int(input("What's n?"))
        if n > 0:
            return n 

def meow(n):
    for _ in range (n):
        print("hi")

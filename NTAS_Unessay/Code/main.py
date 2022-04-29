#   Author: Mathew Hasting
#   NTAS 322
#   April 27, 2022
#   Main file

import Game
import keyboard # For "Press space to continue..." lines

def main():

    ## Intro statement
    print('Hello and welcome to the Jundt Art Museum!')
    print('Welcome to the Jundt Art Museum! You are the guest director for the new Native American religious exhibit!')
    print('The museum has had a lot of trouble coming up with an exhibit that will adequately cover the religious beliefs of Native Americans')
    print('You have been brought on as the guest director because of your extensive knowledge in the field!')
    print('The museum has questions for what to put in each of the five parts of the exhibit and your job is to tell the museum')
    print('what should go in each.')

    ## Code used to pause text and give player time to read, used frequently in Questions.py
    print()
    print('Press space to continue...')
    while True:
        if keyboard.read_key() == 'space':
            break

    ## Decentralize control of program, lets Game.py act as controller
    Game.control()

main()
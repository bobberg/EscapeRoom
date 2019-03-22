# Created by: Bob van den Berg

# escape room garage:
# Via Cem Eser & Samantha van de Molengraft
# Karlijn en Jemma

# It should:
# 1 - It should be full screen on a laptop
# 2 - There should be a beep (sound) every 15 seconds, this will indicate that the participant has to press enter, within a 1 second time window.
# 3 - This should be repeated 7 times
# 4 - If done correctly, the screen should change to green and should show a calculation. There will be a 2 minute time window to type in the correct code
# 5 - If not done correctly (wrong code or in the previous step a beep is missed), the program should reset and start over again.

# TODO 1: Do something if total_seconds left <= 0. Like display text YOU FAIL
# TODO 2: Text input and open website if correct code is inputted.

#!/usr/bin/python3
import time
import playsound
import pygame
from pygame.locals import *
from pygame_functions import *
from sys import exit
import pygame_textinput
import webbrowser
from threading import Timer

# THIS IS TO STOP ALT TAB OR OTHER KEYS TO BE PRESSED
# https://stackoverflow.com/questions/39110800/disable-alttab-combination-on-tkinter-app
# install from: https://sourceforge.net/projects/pyhook/
# import pyHook

# Time constants
TIME_TO_PAUSE = 4

# Different color constants
RED = (255, 0, 0)
RED_ORANGE = (255, 80, 0)
ORANGE = (255, 160, 0)
ORANGE_YELLOW = (255, 200, 0)
YELLOW = (255, 255, 0)
YELLOW_GREEN = (160, 255, 0)
GREENISH = (80, 255, 0)
GREEN = (0, 255, 0)

# Solution
SECRET_CODE = "1234"
URL = 'http://www.python.org/'

# Settings for screen and initialisation.
pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption('ESCAPE ROOM')
background_color = RED
screen.fill(background_color)
counter = 0
background_color = RED
screen.fill(background_color)
clock = pygame.time.Clock()
pygame.time.set_timer(pygame.USEREVENT, 1000)
font = pygame.font.SysFont('Consolas', 30)

textinput = pygame_textinput.TextInput()

# INPUT BOX
input_box = pygame.Rect(100, 100, 140, 32)
color_inactive = pygame.Color('lightskyblue3')
color_active = pygame.Color('dodgerblue2')
color = color_inactive
active = False
text = '0'.rjust(3)
done = False

frame_count = 0
FRAME_RATE = 30
MINUTES_LEFT = 59
SECONDS_LEFT = 4
START_TIME = 3600

frame_count_code_timer = 0
START_VALUE_FOR_COUNTER = 0
TIME_OPEN_FOR_INPUT_CODE = 120  # seconds
sound_played = False

# Problems with the screen
# def reset_counter():
#     counter = 0
#     text = str(counter)
#     background_color = RED
#     screen.fill(background_color)
#     screen.blit(
#         font.render(text.rjust(3), True, (0, 0, 0)),
#         (screen.get_width() // 2, screen.get_height() // 2))

# THIS IS TO STOP ALT TAB OR OTHER KEYS TO BE PRESSED
# def OnKeyboardEvent(event):
#     if event.Key.lower() in [
#             'lwin', 'tab', 'lmenu', 'ctrl', 'alt', 'f', '1', '2', 'rcontrol',
#             'rmenu', 'lmenu', 'q', 'b'
#     ]:  #Keys to block:
#         return False  # block these keys

# # create a hook manager
# hm = pyHook.HookManager()
# # watch for all keyboard events
# hm.KeyDown = OnKeyboardEvent
# # set the hook
# hm.HookKeyboard()


def time_ran_out():
    global out_of_time
    print('You didn\'t answer in time')
    out_of_time = True


while True:

    total_seconds = START_TIME - (frame_count // FRAME_RATE)
    minutes = total_seconds // 60
    seconds = total_seconds % 60
    output_time_string = "Time left: {0:02}:{1:02}".format(minutes, seconds)

    # If time is up, display: YOU LOSE
    if total_seconds <= 0:
        background_color = RED
        screen.fill(background_color)
        screen.blit(
            font.render("YOU LOSE", True, (0, 0, 0)),
            (screen.get_width() // 2, screen.get_height() // 2))
        pygame.display.update()
        for i in range(20):
            time.sleep(5)

    for event in pygame.event.get():
        if total_seconds % 15 == 0 and sound_played == False:
            playsound.playsound("beep.mp3")
            sound_played = True

        elif total_seconds % 15 != 0:
            # Reset variables for every 15 seconds
            sound_played = False
            enter_pressed_once = False

        if event.type == QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.locals.KEYDOWN:
            # counter = START_VALUE_FOR_COUNTER  # FOR TESTING PURPOSES OF CODE WINDOW
            if counter > 7:
                # Display text in middle of screen
                text = 'Input code:'.rjust(3)

                # TODO FOR 2 MINUTES, ELSE RESET COUNTER TO 0
                playsound.playsound("input_code.wav")
                # code_input_total_seconds = TIME_OPEN_FOR_INPUT_CODE - (
                # frame_count_code_timer // FRAME_RATE)
                out_of_time = False
                t = Timer(TIME_OPEN_FOR_INPUT_CODE, time_ran_out)
                t.start()
                while out_of_time == False:
                    # frame_count_code_timer += 1
                    # clock.tick(FRAME_RATE)
                    screenSize(0, 0, fullscreen=True)
                    instructionLabel = makeLabel("Please enter code:", 40, 10,
                                                 10, "blue", "Agency FB",
                                                 "yellow")
                    showLabel(instructionLabel)
                    wordBox = makeTextBox(10, 80, 300, 0, "XXXX", 4, 24)
                    showTextBox(wordBox)

                    entry = textBoxInput(wordBox)
                    if entry == SECRET_CODE:
                        # Open URL in new window, raising the window if possible. Also quit the pygame after the browser has opened.
                        webbrowser.open_new(URL)
                        pygame.quit()
                        quit()
                    else:
                        counter = START_VALUE_FOR_COUNTER
                if out_of_time:
                    hideTextBox(wordBox)
                    print(
                        'this should appear only if input was given in 2 seconds...'
                    )
                    t.cancel()
                    counter = START_VALUE_FOR_COUNTER

            # If pressed enter (can be another button) counter is increased by 1
            elif event.key == pygame.K_RETURN and total_seconds % 15 == 0 and counter <= 7:
                print("enter pressed")
                counter += 1
                enter_pressed_once = False
                text = str(counter)

            elif event.key == pygame.K_RETURN and enter_pressed_once == True:
                # If pressed multiple times per every 15 seconds: Reset counter
                counter = 0
                text = str(counter)
                background_color = RED
                screen.fill(background_color)
                screen.blit(
                    font.render(text.rjust(3), True, (0, 0, 0)),
                    (screen.get_width() // 2, screen.get_height() // 2))

            else:
                # If not pressed every 15 seconds: Reset counter
                counter = 0
                text = str(counter)
                background_color = RED
                screen.fill(background_color)
                screen.blit(
                    font.render(text.rjust(3), True, (0, 0, 0)),
                    (screen.get_width() // 2, screen.get_height() // 2))

            pygame.display.update()

        # For every counter change the color from red towards green.
        if counter == 1:
            background_color = RED_ORANGE
        if counter == 2:
            background_color = ORANGE
        if counter == 3:
            background_color = ORANGE_YELLOW
        if counter == 4:
            background_color = YELLOW
        if counter == 5:
            background_color = YELLOW_GREEN
        if counter == 6:
            background_color = GREENISH
        if counter >= 7:
            background_color = GREEN
        screen.fill(background_color)

    # Remove old text
    screen.fill(background_color)
    # Render text (counter + input)
    screen.blit(
        font.render(text.rjust(3), True, (0, 0, 0)),
        (screen.get_width() // 2, screen.get_height() // 2))
    # Render time left
    screen.blit(font.render(output_time_string, True, (0, 0, 0)), (0, 0))

    frame_count += 1
    clock.tick(FRAME_RATE)
    # pygame.display.update()
    pygame.display.flip()

pygame.quit()
quit()

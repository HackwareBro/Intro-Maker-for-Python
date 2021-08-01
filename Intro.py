from pyfiglet import figlet_format
import colorama
from colorama import Fore, Back, Style
import os
from time import sleep

colorama.init()

#Color changing Title
def blinking(title, cycle=5,color_shade = [Fore.CYAN,Fore.BLUE,Fore.MAGENTA]):   
    for color in range(len(color_shade)*cycle):
        print(color_shade[color%3])
        print(figlet_format(title,font='speed'))
        sleep(0.25)
        os.system('cls')
    print(f'{Fore.RESET}{Back.RESET}') #To reset the colors

#Title rotation
def rotating(title, cycle=5):
    for color in range(4*cycle):
        font = 'isometric' + str(color%4 + 1)
        print(figlet_format(title,font=font))
        sleep(0.25)
        os.system('cls')

#For testing
if __name__ == "__main__":
    blinking('Hackware Bro', 3)
    rotating('HB')
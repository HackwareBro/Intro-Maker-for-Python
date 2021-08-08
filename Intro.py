from pyfiglet import figlet_format
import colorama
from colorama import Fore, Back, Style
import os
from time import sleep

colorama.init()

# ColorName
COLORS = ['BLACK', 'RED', 'GREEN', 'YELLOW', 'BLUE', 'MAGENTA', 'CYAN', 'WHITE']
# Fonts name
FONTS = ['3-d', '3x5', '5lineoblique', 'acrobatic', 'alligator', 'alligator2', 'alphabet', 'avatar', 'banner', 'banner3-D', 'banner3', 'banner4', 'barbwire', 'basic', 'bell', 'big', 'bigchief', 'binary', 'block', 'bubble', 'bulbhead', 'calgphy2', 'caligraphy', 'catwalk', 'chunky', 'coinstak', 'colossal', 'computer', 'contessa', 'contrast', 'cosmic', 'cosmike', 'cricket', 'cursive', 'cyberlarge', 'cybermedium', 'cybersmall', 'diamond', 'digital', 'doh', 'doom', 'dotmatrix', 'drpepper', 'eftichess', 'eftifont', 'eftipiti', 'eftirobot', 'eftitalic', 'eftiwall', 'eftiwater', 'epic', 'fender', 'fourtops', 'fuzzy', 'goofy', 'gothic', 'graffiti', 'hollywood', 'invita', 'isometric1', 'isometric2', 'isometric3', 'isometric4', 'italic', 'ivrit', 'jazmine', 'jerusalem', 'katakana', 'kban', 'larry3d', 'lcd', 'lean', 'letters', 'linux', 'lockergnome', 'madrid', 'marquee', 'maxfour', 'mike', 'mini', 'mirror', 'mnemonic', 'morse', 'moscow', 'nancyj-fancy', 'nancyj-underlined', 'nancyj', 'nipples', 'ntgreek', 'o8', 'ogre', 'pawp', 'peaks', 'pebbles', 'pepper', 'poison', 'puffy', 'pyramid', 'rectangles', 'relief', 'relief2', 'rev', 'roman', 
'rot13', 'rounded', 'rowancap', 'rozzo', 'runic', 'runyc', 'sblood', 'script', 'serifcap', 'shadow', 'short', 'slant', 'slide', 'slscript', 'small', 'smisome1', 'smkeyboard', 'smscript', 'smshadow', 'smslant', 'smtengwar', 'speed', 'stampatello', 'standard', 'starwars', 'stellar', 'stop', 'straight', 'tanja', 'tengwar', 'term', 'thick', 'thin', 'threepoint', 'ticks', 'ticksslant', 'tinker-toy', 'tombstone', 'trek', 'tsalagi', 'twopoint', 'univers', 'usaflag', 'wavy', 'weird'] 

#Color changing Title
def blinking(title, cycle=5,color_shades = [Fore.CYAN,Fore.BLUE,Fore.MAGENTA], font='serifcap'):   
    for color in range(len(color_shades)*cycle):
        print(color_shades[color%3])
        print(figlet_format(title,font=font))
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
    blinking('Hackware Bro', 3, [Fore.CYAN,Fore.RED,Fore.GREEN],'doom')
    rotating('HB')
    print('vist this website to check fonts design: http://www.figlet.org/examples.html')
    input('press any key to exit...')
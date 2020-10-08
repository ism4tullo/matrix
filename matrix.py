from colorama import init, Fore, Style
import random

init()

while 1:
    value = random.random()
    print( Fore.GREEN, Style.DIM + str( value ) * 999999 )
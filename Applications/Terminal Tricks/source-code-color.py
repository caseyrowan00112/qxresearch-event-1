from colorama import init
init()
from colorama import Fore, Back, Style  # Fore: font color | Back: background | Style: text style

print(Fore.GREEN, "hello qxresearcher")

print(Back.RED, "hello qxresearcher")

# To get back to plain black-and-white output: print(Style.RESET_ALL)

# All variations on colors:
# Fore:  BLACK RED GREEN YELLOW BLUE MAGENTA CYAN WHITE RESET
# Back:  BLACK RED GREEN YELLOW BLUE MAGENTA CYAN WHITE RESET
# Style: DIM NORMAL BRIGHT RESET_ALL

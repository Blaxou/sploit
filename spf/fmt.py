# coding=utf-8

clear = '\033[0m'
bold = '\033[1m'
dim = '\033[2m'
ul = '\033[4m'
flash = '\033[5m'
invert = '\033[7m'
hide = '\033[8m'
dflt = '\033[39m'
black = '\033[30m'
gray = '\033[37m'
dGray = '\033[90m'
red = '\033[91m'
green = '\033[92m'
ylw = '\033[93m'
blue = '\033[94m'
mag = '\033[95m'
cyan = '\033[96m'
white = '\033[97m'


def idt(lvl):
    return lvl * "    "


def print_error(string):
    print('\033[91m[-]\033[0m ' + string)


def print_status(string):
    print('\033[94m[*]\033[0m ' + string)


def print_success(string):
    print('\033[92m[+]\033[0m ' + string)


def print_info(string):
    print('\033[93m[?]\033[0m ' + string)

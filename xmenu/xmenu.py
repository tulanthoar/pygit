'''menu to interface with xmonad'''
from sys import stdout
from time import sleep

from click import getchar, command
from pykeyboard import PyKeyboard


def print_flush(text, time=0.001):
    '''print then-flush-for-xmctl'''
    print(text)
    sleep(time)
    stdout.flush()


def print_menu(persist):
    '''print menu of available keys'''
    print_flush('Available cmds')
    print_flush('Spc: next empty ws')
    print_flush('Tab: toggle persist')
    print_flush('  c: clipmenu')
    print_flush('  j: j4-app-menu')
    print_flush('  s: search-engines')
    print_flush('  p: pomodoro')
    print_flush('  t: konsole')
    print_flush('  u: urxvt')
    if persist:
        print_flush('Persistence on')
    else:
        print_flush('Persistence off')


@command()
def xdomenu():
    """interacts with a simple menu."""
    char_to_bin = {'s': 'srmenu',
                   'j': 'jmenu',
                   'c': 'clipmenu',
                   't': 'terminal',
                   'u': 'urxvt',
                   'p': 'pomodoro',
                   ' ': 'moveempty'}
    keybrd = PyKeyboard()
    k_menu = keybrd.menu_key
    persistent = False
    print_menu(persistent)
    while True:
        sleep(0.1)
        stdout.flush()
        char = getchar()
        try:
            cmd = char_to_bin[char]
            print_flush(cmd)
            if persistent:
                sleep(0.2)
                keybrd.tap_key(k_menu)
        except KeyError:
            if char == '\t':
                persistent = not persistent
                print_menu(persistent)
            else:
                keybrd.tap_key(k_menu)

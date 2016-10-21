'''menu to interface with xmonad'''
from sys import stdout
from time import sleep

from click import getchar, command
from pykeyboard import PyKeyboard


def print_flush(text, time=0.01):
    '''print then-flush-for-xmctl'''
    print(text)
    sleep(time)
    stdout.flush()


def print_menu(persist):
    '''print menu of available keys'''
    print_flush('Available cmds')
    print_flush('Spc: next empty ws')
    print_flush('Tab: toggle persist')
    print_flush('  a: all pads')
    print_flush('  b: byobu')
    print_flush('  c: clipmenu')
    print_flush('  h: htop')
    print_flush('  i: ipython')
    print_flush('  j: j4-app-menu')
    print_flush('  n: neovim')
    print_flush('  q: qutebrowser')
    print_flush('  p: perl repl')
    print_flush('  P: pomodoro')
    print_flush('  r: ranger')
    print_flush('  u: urxvt')
    if persist:
        print_flush('Persistence on')
    else:
        print_flush('Persistence off')


@command()
def xdomenu():
    """interacts with a simple menu."""
    char_to_bin = {'q': 'srmenu',
                   'b': 'byobu',
                   'c': 'clipmenu',
                   'j': 'jmenu',
                   'n': 'nvim',
                   'h': 'htop',
                   'u': 'myterm',
                   'i': 'ipython',
                   'p': 'perl',
                   'r': 'ranger',
                   ' ': 'moveempty',
                   'a': 'allpads',
                   'P': 'pomodoro'}
    keybrd = PyKeyboard()
    k_menu = keybrd.menu_key
    persistent = False
    print_menu(persistent)
    while True:
        sleep(0.5)
        stdout.flush()
        char = getchar()
        try:
            cmd = char_to_bin[char]
            # keybrd.tap_key(k_menu)
            print(cmd)
            sleep(0.15)
            stdout.flush()
            if persistent:
                sleep(0.2)
                keybrd.tap_key(k_menu)
        except KeyError:
            if char == '\t':
                persistent = not persistent
                print_menu(persistent)
            else:
                keybrd.tap_key(k_menu)

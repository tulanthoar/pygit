'''menu to interface with xmonad'''
from sys import stdout
from time import sleep

from click import echo, getchar, command
from pykeyboard import PyKeyboard


def print_menu(persist):
    '''print menu of available keys'''
    echo('Spc: next empty ws')
    echo('Tab: toggle persist')
    echo('  a: ll pads')
    echo('  b: byobu')
    echo('  c: clipmenu')
    echo('  h: htop')
    echo('  i: ipython')
    echo('  j: j4-app-menu')
    echo('  n: neovim')
    echo('  q: qutebrowser')
    echo('  p: perl repl')
    echo('  P: pomodoro')
    echo('  r: ranger')
    echo('  u: urxvt')
    if persist:
        echo('Persistence on')
    else:
        echo('Persistence off')


@command()
def xdoprint():
    '''just pring the menu alone'''
    print_menu(False)


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
                   ' ': 'nextempty',
                   'a': 'allpads',
                   'P': 'pomodoro'}
    keybrd = PyKeyboard()
    k_menu = keybrd.menu_key
    persistent = False
    while True:
        char = getchar()
        try:
            opts = char_to_bin[char]
            keybrd.tap_key(k_menu)
            echo(opts)
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

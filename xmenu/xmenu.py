'''menu to interface with xmonad'''
from time import sleep
from click import echo, getchar, command
from sh import Command


def print_menu(persist):
    '''print menu of available keys'''
    echo('Spc: next empty ws')
    echo('Tab: toggle persist')
    echo('  a: all pads')
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
def xdomenu():
    """interacts with a simple menu."""
    xmc = Command('xmctl')
    char_to_bin = {'q': ('srmenu'),
                   'b': ('byobu'),
                   'c': ('clipmenu'),
                   'j': ('jmenu'),
                   'n': ('nvim'),
                   'h': ('htop'),
                   'u': ('myterm'),
                   'i': ('ipython'),
                   'p': ('perl'),
                   'r': ('ranger'),
                   'a': ('allpads'),
                   'P': ('pomodoro')}
    xdo = Command('xdotool')
    persistent = False
    print_menu(persistent)
    while True:
        char = getchar()
        try:
            (opts) = char_to_bin[char]
            xmc('minone')
            xmc(opts)
        except KeyError:
            if char == '\t':
                persistent = not persistent
                print_menu(persistent)
                continue
            elif char == ' ':
                xmc('nextempty')
                continue
        sleep(0.5)
        if persistent:
            xmc('rest')
            continue
        xdo(['key', 'Menu'])
